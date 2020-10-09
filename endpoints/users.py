from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from database.schema import User_Create
from database.model import User
from Tracker import app

@app.post("/api/user/add", response_model=User_Create)
def get_job(user_data: User_Create, db: Session = Depends(get_db)):
    '''
    Add new user to the System

    Args:
        User_Create schema data format provide details to add new user
    Response:
        200 - data of the new user is returned. Data in User_Create schema format
        400 - when user email ID already exists. Response in json data
    '''
    try:
        user = User(**user_data.dict())
        db.add(user)
        db.commit()
        return user
    except:
        raise HTTPException(status_code=400, detail="User already exists")
