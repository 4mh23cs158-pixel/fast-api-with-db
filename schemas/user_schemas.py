from pydantic import BaseModel

class UserSchema(BaseModel):
    username:str
    email:str
    password:str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id:int
    class Config:
        orm_mode=True