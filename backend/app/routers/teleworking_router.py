from fastapi import APIRouter, Depends

from app.models.dto_models import TeleworkingRequest
from app.models.dto_models import TeleworkingRequestCreate
from app.repository.teleworking_repository import TeleworkingRepository
from app.utils.db import get_db

router = APIRouter(prefix="/teleworking", tags=["teleworking"])


def teleworking_repository(db=Depends(get_db)):
    return TeleworkingRepository(db=db)


@router.get("/")
def get_all(
    repo: TeleworkingRepository = Depends(teleworking_repository),
):
    return repo.get_all()


@router.post("/", response_model=TeleworkingRequest)
def create_teleworking_request(
    request: TeleworkingRequestCreate,
    repo: TeleworkingRepository = Depends(teleworking_repository),
):
    return repo.create_teleworking_request(request=request)


@router.put("/{id}/approve", status_code=204)
def approve_teleworking_request(
    id: int, repo: TeleworkingRepository = Depends(teleworking_repository)
):
    repo.approve(id)


@router.put("/{id}/disapprove", status_code=204)
def disapprove_timeoff_request(
    id: int, repo: TeleworkingRepository = Depends(teleworking_repository)
):
    repo.disaprove(id)


@router.delete("/{request_id}")
def delete_teleworking_request(
    request_id: int, repo: TeleworkingRepository = Depends(teleworking_repository)
):
    # a teleworking request can be delete only as long as it was not approved yet
    return repo.delete_teleworking_request(request_id=request_id)
