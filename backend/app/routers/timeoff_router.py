from fastapi import APIRouter, Depends

from app.models.dto_models import TimeOffRequest
from app.models.dto_models import TimeOffRequestCreate
from app.repository.teleworking_repository import TeleworkingRepository
from app.repository.timeoff_repository import TimeoffRepository
from app.utils.db import get_db

router = APIRouter(prefix="/timeoff", tags=["timeoff"])


def timeoff_repository(db=Depends(get_db)):
    return TimeoffRepository(db=db)


@router.get("/")
def get_all(
    repo: TimeoffRepository = Depends(timeoff_repository)
):
    return repo.get_all()


@router.post("/", response_model=TimeOffRequest)
def create_timeoff_request(
    request: TimeOffRequestCreate, repo: TimeoffRepository = Depends(timeoff_repository)
):
    return repo.create_time_off_request(request=request)


@router.put("/{id}/approve", status_code=204)
def approve_timeoff_request(
    id: int, repo: TimeoffRepository = Depends(timeoff_repository)
):
    repo.approve(id)


@router.put("/{id}/disapprove", status_code=204)
def disapprove_timeoff_request(
    id: int, repo: TimeoffRepository = Depends(timeoff_repository)
):
    repo.disapprove(id)


@router.delete("/{request_id}")
def delete_timeoff_request(
    request_id: int, repo: TimeoffRepository = Depends(timeoff_repository), status_code=204
):
    # a timeoff request can be delete only as long as it was not approved yet
    repo.delete_time_off_request(request_id=request_id)
