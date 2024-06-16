import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from app.models.dto_models import UserRegister, MessageResponse, UserLogin
from app.repository.user_repository import UsersRepository
from app.utils.db import get_db

router = APIRouter(prefix="/users", tags=["users"])


def users_repository(db=Depends(get_db)):
    return UsersRepository(db=db)


def get_password_hash(password: str) -> str:
    # todo add hasing here
    return password


def verify_password(real_password: str, login_password: str) -> bool:
    login_password_hased = get_password_hash(login_password)
    if real_password == login_password_hased:
        return True
    else:
        return False


@router.get("/")
def get_all(db: UsersRepository = Depends(users_repository)):
    all = db.get_all()
    return [
        {"id": user.id, "full_name": user.full_name, "email": user.email_address, "role": user.role} for user in all
    ]


@router.post("/register", response_model=MessageResponse)
def register_user(
    user: UserRegister, repo: UsersRepository = Depends(users_repository)
):
    db_user = repo.get_user_id_by_email_or_username_and_role(
        user.username, user.email, user.role
    )
    if db_user is not None:
        return JSONResponse(
            status_code=400,
            content=jsonable_encoder(
                MessageResponse(
                    message="User with email or username already registered for given role."
                )
            ),
        )
    user.password = get_password_hash(user.password)
    repo.insert_user(user)
    return MessageResponse(message="User registered")


@router.post("/login")
def login(user_login: UserLogin, db: UsersRepository = Depends(users_repository)):
    user = db.get_user_by_username(user_login.username)
    if not user or not verify_password(real_password=user.password, login_password=user_login.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = jwt.encode({"user": user.username}, "very-secret-secret", algorithm="HS256")
    return {"message": "Login successful", "token": token, "user_id": user.id, "role": user.role, "full_name": user.full_name}
