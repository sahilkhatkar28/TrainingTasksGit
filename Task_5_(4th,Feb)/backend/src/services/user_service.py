# BACKEND/src/services/user_service.py
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from src.config.config import ALGORITHM,SECRET_KEY
from src.models.user_model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        name: str = payload.get("name")
        if email is None:
            raise credentials_exception
        user = User(email=email, name=name)
        return user
    except jwt.PyJWTError:
        raise credentials_exception