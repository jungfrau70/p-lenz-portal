from sqlalchemy.orm import Session
from cruds import models
from routers import schemas
from fastapi import HTTPException,status
from io import BytesIO

import pandas as pd
import numpy as np

from utils.hashing import Hash
from utils import token

Model = models.User
Schema = schemas.ShowUser


def get_all(db: Session):
    users = db.query(Model).all()
    return users

def register(request: Schema,db:Session):
    new_record = Model(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
        )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

def login(request: Schema, db: Session):
    user = db.query(Model).filter(Model.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    access_token = token.create_access_token(data={"sub": user.email})   
    return { "access_token": access_token, "token_type": "bearer" }

def refresh(id:int,request, db:Session):
    user = db.query(Model).filter(Model.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    access_token = token.create_access_token(data={"sub": user.email})   
    return { "access_token": access_token, "token_type": "bearer" }

def destroy(id:int,db: Session):
    record = db.query(Model).filter(Model.id == id)

    if not record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with id {id} not found")

    # record.delete(synchronize_session=False)
    db.query(Model).filter(Model.id == id).delete()
    db.commit()
    return 'done'

def get(id:int,request, db:Session):
    user = db.query(Model).filter(Model.email == request.username).first()    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"record with the id {id} is not available")
    return user        