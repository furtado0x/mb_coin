from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

from mocks.mock_bd_auth import AUTHORIZED_USERS


security = HTTPBasic()

def verify_password(plain_password, hashed_password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    hashed_password = AUTHORIZED_USERS.get(credentials.username)
    if not hashed_password or not verify_password(credentials.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
