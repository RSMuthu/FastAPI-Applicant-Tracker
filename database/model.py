## DB Models definitions
from sqlalchemy import Boolean, DateTime, Column, Text, Integer, String
from datetime import datetime

from .db import Base

class Job(Base):
    '''
    Model - Job
    Table for Jobs -- holds all the information of the jobs created
    '''
    __tablename__ = "Job"
    id = Column(Integer, primary_key=True, autoincrement=True)
    creator = Column(String(100), nullable=False) ## Make this foreign key when implementing with multiple users
    desc = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    company_name = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False) ## can change this into a geo plot (gson)
    is_applied = Column(Boolean, nullable=False, default=False)
    apply_date = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"Title - {job_title}"

class User(Base):
    '''
    Model - User
    Table for USers -- holds the information of the users
    '''
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False, unique=True)
    is_recruiter = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"{email} -- RECRUITER ({is_recruiter})"
