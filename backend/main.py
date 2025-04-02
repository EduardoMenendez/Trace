from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
import tempfile
import shutil
import os
import json
from pathlib import Path

from controller import run_wfuzz_and_build_tree, save_tree_to_file

app = FastAPI()

@app.get("/")
def get():
    return {"code": 200, "message": "Hello World 23"}


@app.post("/crawl")
async def crawl(
    target_url: str = Form(...),
    user_agent: str = Form(None),
    proxy: str = Form(None),
    delay: float = Form(0),
    dictionary: UploadFile = File(...),
    project_id: str = Form(...)
):
    # Save the uploaded file to a temporary file
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            shutil.copyfileobj(dictionary.file, tmp)
            tmp_path = tmp.name
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to process uploaded file: {str(e)}"})

    try:
        tree = run_wfuzz_and_build_tree(
            target_url=target_url,
            wordlist=tmp_path,
            user_agent=user_agent,
            proxy=proxy,
            delay=delay
        )
        if tree:
            save_tree_to_file(tree, project_id, target_url=target_url)
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