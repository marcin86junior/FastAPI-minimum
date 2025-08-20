from typing import Annotated

from jwt.exceptions import InvalidTokenError
from auth.models.token import TokenData
from auth.utils.auth_utils import verify_password
from core.config_loader import settings
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta, timezone
import jwt
from core.database import get_db
from user.models.user import User
from user.services.user_service import get_user_by_email

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def authenticate_user(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            return None
        user = get_user_by_email(db, email)
        if user is None:
            return None
        return user
    except InvalidTokenError:
        return None


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db:Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


def authenticate_user_by_credentials(db: Session, username: str, password: str):
    # Próba znalezienia użytkownika po emailu
    user = get_user_by_email(db, username)

    # Jeśli nie znaleziono po emailu, spróbuj po nazwie użytkownika
    if not user:
        user = db.query(User).filter(User.username == username).first()

    # Sprawdź hasło jeśli znaleziono użytkownika
    if not user or not verify_password(password, user.hashed_password):
        return None

    return user