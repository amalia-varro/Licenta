from typing import Optional
from datetime import date
from sqlalchemy.orm import Session
from app.models.dto_models import WorkLogCreate
from app.models.orm_models import WorkLog


class WorklogRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_worklog(self, worklog: WorkLogCreate):
        db_worklog = WorkLog(**worklog.dict())
        self.db.add(db_worklog)
        self.db.commit()
        self.db.refresh(db_worklog)
        return db_worklog

    def get_worklogs(
        self, user_id: int, date: Optional[date] = None, year: Optional[int] = None
    ):
        query = self.db.query(WorkLog).filter(WorkLog.user_id == user_id)
        if date:
            query = query.filter(WorkLog.date == date)
        if year:
            query = query.filter(WorkLog.date.year == year)
        return query.all()

    def get_all(self):
        return self.db.query(WorkLog).all()
