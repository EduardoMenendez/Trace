from typing import List
from pydantic import BaseModel

class Project(BaseModel):
    id: str
    name: str
    owner: str
    is_locked: bool = False
    files: List[str] = []
    ip_list: List[str] = []

    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False