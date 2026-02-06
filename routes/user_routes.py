from fastapi import APIRouter

router=APIRouter()

@router.post("/signup")
def signup():
    return {"message":"signup SUCCESSFULL"}

@router.post("/login")
def login():
    return {"message":"login SUCCESSFULL"}

@router.post("/logout")
def logout():
    return {"message":"logout SUCCESSFULL"}