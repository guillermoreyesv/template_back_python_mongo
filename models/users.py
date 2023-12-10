from pydantic import BaseModel
from typing import List

# Define Pydantic models for the data
class UserBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: str
    phone_number: str
    email: str
    password: str
    profile_picture: str

class User(UserBase):
    id: str
    type: str
    social_media: dict = {}
    display_name: str = ""
    default_location: dict = {}