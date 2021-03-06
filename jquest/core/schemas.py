from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    name: str
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    class Config:
        orm_mode = True