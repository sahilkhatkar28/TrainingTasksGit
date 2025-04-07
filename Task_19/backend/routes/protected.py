from fastapi import APIRouter, Depends, HTTPException, Header
from auth import decode_access_token

router = APIRouter()

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=403, detail="Not authenticated")
    
    token = authorization.split(" ")[1]
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return payload.get("sub")

@router.get("/protected")
def protected_route(user: str = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": user}
