import datetime

from sqlalchemy.orm import Session

from app.models.dto_models import TimeOffRequestCreate
from app.models.orm_models import TimeOffRequest


class TimeoffRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(TimeOffRequest).all()

    def create_time_off_request(self, request: TimeOffRequestCreate):
        db_request = TimeOffRequest(**request.dict(), request_date=datetime.datetime.now(), status="pending")
        self.db.add(db_request)
        self.db.commit()
        self.db.refresh(db_request)
        return db_request

    def delete_time_off_request(self, request_id: int):
        db_request = self.db.query(TimeOffRequest).filter_by(id=request_id).first()
        if db_request:
            self.db.delete(db_request)
            self.db.commit()

    def approve(self, id):
        db_request = self.db.query(TimeOffRequest).filter_by(id=id).first()
        if db_request:
            db_request.status = "approved"
            self.db.add(db_request)
            self.db.commit()

    def disapprove(self, id):
        db_request = self.db.query(TimeOffRequest).filter_by(id=id).first()
        if db_request:
            db_request.status = "disapproved"
            self.db.add(db_request)
            self.db.commit()
