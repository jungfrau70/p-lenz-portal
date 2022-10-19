from fastapi import APIRouter
from . import schemas
from config import database
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from cruds import user

router = APIRouter(
    prefix="/account",
    tags=['Users']
)

get_db = database.get_db


@router.post('/register', response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)
