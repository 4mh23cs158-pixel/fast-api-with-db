from fastapi import APIRouter
from sqlalchemy.orm import Session
from db import get_db
from fastapi import Depends
from repositories.user_repo import UserRepo

router=APIRouter()

@router.post("/signup")
def signup(db:Session=Depends(get_db)):
    user_repo=UserRepo(db)
    user_repo.add_user()
    return{"message":"user added successfully"}
    
@router.post("/login")
def login():
    return {"message":"login SUCCESSFULL"}

@router.post("/logout")
def logout():
    return {"message":"logout SUCCESSFULL"}