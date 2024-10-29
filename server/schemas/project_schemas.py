from datetime import datetime
from pydantic import BaseModel


class NewProjectRequest(BaseModel):
    title: str
    status: str = 'new'
    descrption: str = ''  # Con las '' le damos un valor por defecto


class ProjectRequest(BaseModel):
    title: str | None = None
    status: str | None = None
    descrption: str | None = None


class ProjectResponse(BaseModel):
    id: int
    title: str
    status: str = 'new'
    descrption: str = ''
    created_at: datetime
    updated_at: datetime
