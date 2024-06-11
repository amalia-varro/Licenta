import typing

from sqlalchemy import text, insert
from sqlalchemy.orm import Session

from app.models.orm_models import User

from app.models.dto_models import UserRegister


class UsersRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(User).all()

    def get_user_by_username(self, username: str) -> typing.Optional[User]:
        user = self.db.query(User).filter(User.username == username).first()
        if user:
            return user
        return None

    def get_user_by_id_and_role(self, id: int, role: str) -> typing.Optional[User]:
        user = self.db.query(User).filter(User.id == id, User.role == role).first()
        if user:
            return user
        return None

    def get_user_id_by_email_or_username_and_role(
        self, username: str, email: str, role: str
    ) -> typing.Optional[User]:
        statement = text(
            """SELECT * from "users" WHERE (username = :username OR email_address = :email) AND role = :role"""
        ).bindparams(
            username=username,
            email=email,
            role=role,
        )
        user = self.db.execute(statement).first()
        if user:
            return user[0]
        return None

    def get_full_name_by_id(self, id: int) -> typing.Optional[str]:
        user = self.db.query(User).filter(User.id == id).first()
        if user:
            return user.full_name
        return None

    def insert_user(self, user: UserRegister):
        statement = insert(User).values(
            role=user.role,
            username=user.username,
            password=user.password,
            full_name=user.full_name,
        )
        self.db.execute(statement=statement)
        self.db.commit()
