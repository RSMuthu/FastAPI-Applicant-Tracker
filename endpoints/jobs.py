## Different Endpoints for Job(s)
from datetime import datetime
from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from database.schema import Job_Scheme, Job_Create
from database.model import Job, User
from Tracker import app

@app.get("/api/jobs", response_model=List[Job_Scheme])
def get_jobs_list(db: Session = Depends(get_db)):
    '''
    Get the list of all the jobs available.

    Response:
        list of all the jobs. data in the Job_Scheme schema Format
    '''
    jobs = db.query(Job).all()
    return jobs

@app.post("/api/job", response_model=Job_Scheme)
def create_job(job: Job_Create, req: Request, db: Session = Depends(get_db)):
    '''
    Creates a new job

    Args:
        Data in Job_Create schema format
    Response:
        200 - data of the Job created. Data in Job_Scheme schema format
        401 - when  the user who creates the job is a Candidate and not a recruiter
    '''
    auth_header = req.headers['Authorization'].split()
    if auth_header[0] == "user":
        req_user = auth_header[1]
    else:
        raise HTTPException(status_code=401, detail="Invalid Authorization Header !")
    job_dict = job.dict()
    if job_dict['creator'] != req_user:
        raise HTTPException(status_code=401, detail="User not permitted.. Job Creator & Auth header are pointing different person")
    user = db.query(User).filter(User.email == job_dict['creator']).first()
    if not user or not user.is_recruiter:
        raise HTTPException(status_code=401, detail="User not permitted")
    job_item = Job(**job_dict)
    db.add(job_item)
    db.commit()
    db.refresh(job_item)
    return job_item

@app.get("/api/job/{job_id}", response_model=Job_Scheme)
def get_job(job_id: int, db: Session = Depends(get_db)):
    '''
    Get the job details of the job id provided

    Args:
        id - Job ID for which the job is to be fetched
    Response:
        200 - data of the job requested. Data in Job_Scheme schema format
        404 - when the job is not found (Json format)
    '''
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.delete("/api/job/{job_id}")
def delete_job(job_id: int, req: Request, db: Session = Depends(get_db)):
    '''
    Delete the job from the DB corresponding to the Job id provided.

    Args:
        id - Job ID whose job is to be deleted from the DB
    Response:
        200 - Json message stating the success
        404 - When the job is not found (Json Format)
        401 - when the user is a candidate, not supposed to delete the job
    '''
    auth_header = req.headers['Authorization'].split()
    if auth_header[0] == "user":
        req_user = auth_header[1]
    else:
        raise HTTPException(status_code=401, detail="Invalid Authorization Header !")
    user = db.query(User).filter(User.email == req_user).first()
    if not user or not user.is_recruiter:
        raise HTTPException(status_code=401, detail="User not permitted")
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(job)
    db.commit()
    return {'msg': "Deletion successful"}

@app.put("/api/job/{job_id}")
def apply_job(job_id: int, req: Request, db: Session = Depends(get_db)):
    '''
    Apply to the job whose Job id is provided

    Args:
        id - JOb ID to which you want to apply
    Response:
        200 - json message of successful apply
        404 - when the Job ID is not found (Json Format)
        400 - when the user has already applied for the job
        401 - when the user is a recruiter who is not supposed to apply
    '''
    auth_header = req.headers['Authorization'].split()
    if auth_header[0] == "user":
        req_user = auth_header[1]
    else:
        raise HTTPException(status_code=401, detail="Invalid Authorization Header !")
    user = db.query(User).filter(User.email == req_user).first()
    if not user or user.is_recruiter:
        raise HTTPException(status_code=401, detail="User not permitted")
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.is_applied:
        raise HTTPException(status_code=400, detail="You have already applied to this job")
    job.is_applied = True
    job.apply_date = datetime.utcnow()
    db.commit()
    return {'msg': "Job Apply is successful"}
