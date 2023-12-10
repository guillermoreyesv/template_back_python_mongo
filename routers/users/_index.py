# Main router

from fastapi import APIRouter
from models.users import User,UserBase
from .register_new_user import router as register_new_user

router = APIRouter()

router.include_router(register_new_user)

"""
@router.get("/{user_id}")
def view_user(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    return {"message": "ok"}

@router.patch("/{user_id}")
def edit_user(user: UserBase):
    return {"message": "ok"}


@router.delete("/{user_id}")
def cancel_account(user: UserBase):
    return {"message": "ok"}


@router.post("/login")
def login_user(email: str, password: str):
    user_info = login(email, password)
    if user_info:
        return user_info
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/{user_id}/events")
def view_user_events(user: UserBase):
    return {"message": "ok"}
"""