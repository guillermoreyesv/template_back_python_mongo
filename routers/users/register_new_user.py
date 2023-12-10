from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response as Resp

from models.users import UserBase

router = APIRouter()

@router.post("/")
def register_new_user(user: UserBase):
    user_data = user.model_dump()
    user_id = validate(user_data)
    return {"message": "User registered successfully", "user_id": user_id}

def validate(user = {}):
    return user