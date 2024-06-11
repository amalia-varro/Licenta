from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends

from app.models.dto_models import WorkLog
from app.models.dto_models import WorkLogCreate
from app.repository.worklog_repository import WorklogRepository
from app.utils.db import get_db

router = APIRouter(prefix="/worklog", tags=["worklog"])


def worklog_repository(db=Depends(get_db)):
    return WorklogRepository(db=db)


@router.get("/")
def get_all(
    repo: WorklogRepository = Depends(worklog_repository)
):
    return repo.get_all()


@router.post("/", response_model=WorkLog)
def create_worklog(
    worklog: WorkLogCreate, repo: WorklogRepository = Depends(worklog_repository)
):
    return repo.create_worklog(worklog=worklog)


@router.get("/{user_id}", response_model=List[WorkLog])
def read_worklogs(
    user_id: int,
    date: Optional[date] = None,
    year: Optional[int] = None,
    repo: WorklogRepository = Depends(worklog_repository),
):
    return repo.get_worklogs(user_id=user_id, date=date, year=year)
