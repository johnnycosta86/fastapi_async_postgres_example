from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app.src.core import security
from app.src.core.config import settings
# from app.src.core.security import get_current_active_user
from app.src.models.user import User
from app.src.schemas.user_dto import UserDTO, UserCreate, UserUpdate
from app.src.crud.crud_user import crudUser
from app.src.api import deps

router = APIRouter()


@router.get("/", response_model=List[UserDTO])
def read_users(db: Session = Depends(deps.get_db)) -> Any:
    """
    Retrieve users.
    """
    users = crudUser.get_multi(db)
    return users


@router.post("/", response_model=UserDTO)
def create_user(*, db: Session = Depends(deps.get_db), user_in: UserCreate) -> Any:
    """
    Create new user.
    """
    user = crudUser.get_by_email(db, email=user_in.email)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    user = crudUser.create(db, obj_in=user_in)

    return user


# @router.put("/me", response_model=UserDTO)
# def update_user_me(*, db: Session = Depends(deps.get_db), password: str = Body(None), full_name: str = Body(None),
#                    email: EmailStr = Body(None),
#                    current_user: User = Depends(deps.get_current_active_user)) -> Any:
#     """
#     Update own user.
#     """
#     current_user_data = jsonable_encoder(current_user)
#     user_in = UserUpdate(**current_user_data)
#     if password is not None:
#         user_in.password = password
#     if full_name is not None:
#         user_in.full_name = full_name
#     if email is not None:
#         user_in.email = email
#     user = crudUser.update(db, db_obj=current_user, obj_in=user_in)
#     return user


# @router.get("/me", response_model=UserDTO)
# def read_user_me(db: Session = Depends(deps.get_db), current_user: User = Depends(deps.get_current_active_user)) -> Any:
#     """
#     Get current user.
#     """
#     return current_user


@router.post("/open", response_model=UserDTO)
def create_user_open(*, db: Session = Depends(deps.get_db), password: str = Body(...), email: EmailStr = Body(...),
                     full_name: str = Body(None)) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(status_code=403, detail="Open user registration is forbidden on this server")
    user = crudUser.get_by_email(db, email=email)
    if user:
        raise HTTPException(status_code=400, detail="The user with this username already exists in the system")
    user_in = UserCreate(hashed_password=password, email=email, full_name=full_name)
    user = crudUser.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=UserDTO)
def read_user_by_id(user_id: int, db: Session = Depends(deps.get_db)) -> Any:
    """
    Get a specific user by id.
    """
    user = crudUser.get(db, id=user_id)

    if user:
        return user
    else:
        raise HTTPException(status_code=400, detail="User Not Found!")


@router.put("/{user_id}", response_model=UserDTO)
def update_user(*, db: Session = Depends(deps.get_db), user_id: int, user_in: UserUpdate) -> Any:
    """
    Update a user.
    """
    user = crudUser.get(db, id=user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )

    user = crudUser.update(db, db_obj=user, obj_in=user_in)

    return user


# # @router.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user
