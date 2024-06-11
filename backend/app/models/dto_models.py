from pydantic import BaseModel
from typing import Optional
from datetime import date, time


class MessageResponse(BaseModel):
    message: str


class UserLogin(BaseModel):
    username: str  # usernames are unique across users
    password: str


class UserRegister(BaseModel):
    full_name: str
    username: str
    email: str
    role: str = "tourist"
    phone_number: str
    password: str


class WorkLogBase(BaseModel):
    user_id: int
    project_id: int
    date: date
    start_hour: time
    end_hour: time
    break_start_hour: Optional[time]
    break_end_hour: Optional[time]


class WorkLogCreate(WorkLogBase):
    pass


class WorkLog(WorkLogBase):
    class Config:
        from_attributes = True


class TeleworkingRequestBase(BaseModel):
    user_id: int
    date: date

class TeleworkingRequestCreate(TeleworkingRequestBase):
    pass


class TeleworkingRequest(TeleworkingRequestBase):
    class Config:
        from_attributes = True


class TimeOffRequestBase(BaseModel):
    user_id: int
    start_date: date
    end_date: date


class TimeOffRequestCreate(TimeOffRequestBase):
    pass


class TimeOffRequest(TimeOffRequestBase):
    id: int

    class Config:
        from_attributes = True
