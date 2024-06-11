import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    func,
    DateTime,
    Boolean,
    ForeignKey,
    Date,
    Time,
    Interval,
    JSON,
)
from sqlalchemy.dialects.postgresql import ENUM

from app.utils.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50))
    username = Column(String(50))
    password = Column(String(200))
    full_name = Column(String(50))  # separated by spaces
    email_address = Column(String(50))  # needs validation
    password_hash = Column(String(50))
    created = Column(
        DateTime(timezone=True), server_default=func.now()
    )  # calculate timestamp on server side
    deleted = Column(Boolean, default=False, nullable=False)


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class WorkLog(Base):
    __tablename__ = "worklogs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    date = Column(Date)
    start_hour = Column(Time)
    end_hour = Column(Time)
    break_start_hour = Column(Time)
    break_end_hour = Column(Time)


class TeleworkingRequest(Base):
    __tablename__ = "teleworking_requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date)
    status = Column(String(50))
    request_date = Column(DateTime)


class TimeOffRequest(Base):
    __tablename__ = "time_off_requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(50))
    request_date = Column(DateTime)
