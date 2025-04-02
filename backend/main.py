from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import tempfile
import shutil
import os
import json
from pathlib import Path

from services.project_service import ProjectService
from services.scan_service import ScanService
from models.project import Project

app = FastAPI()
project_service = ProjectService()
scan_service = ScanService()

@app.get("/")
def get():
    return {"code": 200, "message": "Hello World 23"}

@app.post("/projects")
def create_project(project: Project):
    created_project = project_service.create_project(project.name, project.owner)
    return created_project

@app.get("/projects/{project_id}")
def get_project(project_id: str):
    project = project_service.get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.put("/projects/{project_id}")
def update_project(project_id: str, project: Project):
    updated_project = project_service.update_project(project_id, project)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

@app.delete("/projects/{project_id}")
def delete_project(project_id: str):
    deleted = project_service.delete_project(project_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}

@app.post("/projects/{project_id}/crawl")
async def crawl(
    project_id: str,
    target_url: str = Form(...),
    user_agent: str = Form(None),
    proxy: str = Form(None),
    delay: float = Form(0),
    dictionary: UploadFile = File(...)
):
    project = project_service.get_project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Save the uploaded file to a temporary file
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            shutil.copyfileobj(dictionary.file, tmp)
            tmp_path = tmp.name
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to process uploaded file: {str(e)}"})
    
    try:
        tree = scan_service.run_wfuzz(target_url, tmp_path, user_agent, proxy, delay)
        if tree:
            scan_service.save_tree_to_file(tree, project_id, target_url)
            return {"success": "Crawl Done Successfully"}
        else:
            return JSONResponse(status_code=500, content={"error": "Failed to run wfuzz or build tree."})
    finally:
        # Clean up the temporary file
        os.unlink(tmp_path)

@app.get("/projects/{project_id}/crawls")
def list_project_outputs(project_id: str):
    """
    Lists all output folders for a given project ID.
    """
    base_path = Path("output") / project_id
    if not base_path.exists() or not base_path.is_dir():
        raise HTTPException(status_code=404, detail="Project not found or has no outputs.")
    
    folders = []
    for folder in base_path.iterdir():
        if folder.is_dir():
            folders.append({
                "host": folder.name,
                "path": str(folder),
                "tree_file": str(folder / "tree.json") if (folder / "tree.json").exists() else None
            })
    
    return JSONResponse(content={"project_id": project_id, "targets": folders})

@app.get("/projects/{project_id}/outputs/{host}/tree")
def get_tree_json(project_id: str, host: str):
    """
    Returns the contents of the tree.json file for a specific project and host.
    """
    tree_path = Path("output") / project_id / host / "tree.json"
    if not tree_path.exists():
        raise HTTPException(status_code=404, detail="Tree JSON not found.")
    
    try:
        with open(tree_path, "r") as f:
            tree_data = json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")
    
    return JSONResponse(content=tree_data)