from fastapi import APIRouter, Depends

from app.repository.projects import ProjectsRepository
from app.utils.db import get_db

router = APIRouter(prefix="/projects", tags=["projects"])


def projects_repository(db=Depends(get_db)):
    return ProjectsRepository(db=db)


@router.post("/", response_model=dict)
def create_project(
    project_name: str,
    repo: ProjectsRepository = Depends(projects_repository),
):
    project = repo.create_project(name=project_name)
    return {
        "id": project.id,
        "name": project.name
    }


@router.get("/")
def get_projects(
    repo: ProjectsRepository = Depends(projects_repository),
):
    projects = repo.get_all()
    return list(map(lambda x: {"id": x.id, "name": x.name}, projects))


@router.delete("/", status_code=204)
def create_project(
    project_id: int,
    repo: ProjectsRepository = Depends(projects_repository),
):
    repo.delete_project(project_id)
