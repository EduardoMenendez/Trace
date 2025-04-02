from models.project import Project
from typing import List

class ProjectService:
    def __init__(self):
        self.projects: List[Project] = []

    def create_project(self, name: str, owner: str) -> Project:
        project = Project(id=str(len(self.projects) + 1), name=name, owner=owner)
        self.projects.append(project)
        return project

    def get_project_by_id(self, project_id: str) -> Project:
        return next((p for p in self.projects if p.id == project_id), None)

    def update_project(self, project_id: str, project: Project) -> Project:
        existing_project = self.get_project_by_id(project_id)
        if existing_project:
            existing_project.name = project.name
            existing_project.owner = project.owner
            existing_project.is_locked = project.is_locked
            existing_project.files = project.files
            existing_project.ip_list = project.ip_list
        return existing_project

    def delete_project(self, project_id: str) -> bool:
        project = self.get_project_by_id(project_id)
        if project:
            self.projects.remove(project)
            return True
        return False