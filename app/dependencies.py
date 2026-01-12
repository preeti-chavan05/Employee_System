from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = "SECRET123"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def admin_only(user=Depends(get_current_user)):
    if user["role"] not in ["Admin", "HR"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return user
