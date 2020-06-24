# from datetime import timedelta
# from typing import Any
#
# import jwt
# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jwt import PyJWTError
#
# from sqlalchemy.orm import Session
#
# from app.src.api import deps
# from app.src.core import security
# from app.src.core.config import settings, Settings
# from app.src.crud.crud_user import crudUser
# from app.src.models.user import User
# from app.src.schemas.token_dto import Token, TokenData
# from app.src.schemas.user_dto import UserDTO
#
# router = APIRouter()
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
#
#
# @router.post("/token", response_model=Token)
# async def login_for_access_token(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
#     print("/token-> login_for_access_token")
#     user = crudUser.authenticate(db, email=form_data.username, password=form_data.password)
#
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     access_token_expires = timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     # access_token = security.create_access_token(user.id, expires_delta=access_token_expires)
#     access_token = security.create_access_token(user.email, expires_delta=access_token_expires)
#
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
#
