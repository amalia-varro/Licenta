from sqlalchemy.orm import Session

from app.models.orm_models import Project


class ProjectsRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, name: str) -> Project:
        project = Project(name=name)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def get_all(self):
        return self.db.query(Project).all()

    def delete_project(self, project_id: int):
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if project:
            self.db.delete(project)
            self.db.commit()
