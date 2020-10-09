## Define the DB schemas to get the data serialised to/from ORM
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class Job_Create(BaseModel):
    '''
    Scheme for the data used to Create Job
    '''
    title: str
    company_name: str
    creator: EmailStr
    location: str
    desc: str

class Job_Scheme(Job_Create):
    '''
    Schema Used when pulling data from/to the ORM tables
    '''
    id: int
    create_date: datetime
    is_applied: bool
    apply_date: Optional[datetime] = None

    class Config:
        '''
        Config for Schema to mention thats its might be from ORM
        '''
        orm_mode = True

class User_Create(BaseModel):
    '''
    Scheme for data used to create/represent User <--> ORM table
    '''
    email: EmailStr
    is_recruiter: bool

    class Config:
        '''
        This schema shall be used to fetch from ORM table as well.
        '''
        orm_mode = True
