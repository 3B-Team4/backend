# Used for querying database

from enum import Enum
from pydantic import BaseModel, Field, EmailStr

import logging
logger = logging.getLogger(__name__)
class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    userType: bool

    class Config:
        orm_mode = True

class RoomSchema(BaseModel):
    id: int
    name: str
    roomName: str

    class Config:
        orm_mode = True
