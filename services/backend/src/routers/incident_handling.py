from typing import List, Union
from fastapi import APIRouter,Depends,status,HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from pandas_ods_reader import read_ods

from config import database
from routers import schemas
from utils import oauth2
from sqlalchemy.orm import Session
from cruds import incident_handling

router = APIRouter(
    prefix="/incident",
    tags=['Incident Handling']
)

get_db = database.get_db
from auth.authentications import get_current_active_user

SchemaShow = schemas.ShowIncident
Schema = schemas.Incident

@router.get('/all', response_model=List[SchemaShow])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    print(current_user.__dict__)
    return incident_handling.get_all(db, current_user)

@router.get('/{id}', status_code=200, response_model=Schema)
def show(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    return incident_handling.show(id, db, current_user)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Schema, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    return incident_handling.create(request, db, current_user)

@router.post('/uploadfile', status_code=status.HTTP_201_CREATED,)
async def upload_file(file: Union[UploadFile, None] = None, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    if file.filename.lower().endswith(('.csv')):
        return incident_handling.upload_csv(file, db, current_user)
    else:
        return {"message": "No csv upload file sent"} 

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    return incident_handling.destroy(id, db, current_user)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: Schema, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    return incident_handling.update(id,request, db, current_user)
