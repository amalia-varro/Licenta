import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.orm_models import TeleworkingRequest
from app.models.dto_models import TeleworkingRequestCreate


class TeleworkingRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(TeleworkingRequest).all()

    def create_teleworking_request(self, request: TeleworkingRequestCreate):
        db_request = TeleworkingRequest(**request.dict(), request_date=datetime.datetime.now(), status="pending")
        self.db.add(db_request)
        self.db.commit()
        self.db.refresh(db_request)
        return db_request

    def delete_teleworking_request(self, request_id: int):
        db_request = (
            self.db.query(TeleworkingRequest)
            .filter(
                TeleworkingRequest.id == request_id,
                TeleworkingRequest.status == "pending",
            )
            .first()
        )
        if db_request:
            self.db.delete(db_request)
            self.db.commit()
            return {"message": "Request deleted"}
        raise HTTPException(
            status_code=404, detail="Request not found or not in pending status"
        )

    def approve(self, id):
        response: TeleworkingRequest | None = (
            self.db.query(TeleworkingRequest)
            .filter(TeleworkingRequest.id == id)
            .first()
        )
        if response:
            response.status = "approved"
            self.db.add(response)
            self.db.commit()

    def disaprove(self, id):
        response: TeleworkingRequest | None = (
            self.db.query(TeleworkingRequest)
            .filter(TeleworkingRequest.id == id)
            .first()
        )
        if response:
            response.status = "disapproved"
            self.db.add(response)
            self.db.commit()
