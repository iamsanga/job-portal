
from sqlalchemy.orm import Session

from backend import models, schemas

def received_jobs(db: Session):
    records = db.query(models.JobInfo).filter(models.JobInfo.applied > 0).all()
    return records

    
def read_jobs(db: Session):
    records = db.query(models.JobInfo).all()
    return records

def apply_job(db: Session, job_id:int):
   apply = db.query(models.JobInfo).filter(models.JobInfo.id == job_id).first()
   apply.applied += 1
   db.commit()
   db.refresh(apply)

def update_job(db: Session, job_id:int, job: schemas.JobInfoBase):
   update = db.query(models.JobInfo).filter(models.JobInfo.id == job_id).first()
   update.jobname = job.jobname
   update.description = job.description
   update.location = job.location
   db.commit()
   db.refresh(update)
   return update


def create_job(db: Session, job: schemas.JobInfoBase):

    add_job = models.JobInfo(jobname=job.jobname, description=job.description,
    location=job.location,applied= 0)

    db.add(add_job)
    db.commit()
    db.refresh(add_job)
    return add_job

def delete_job(db: Session, job_id:int):

   del_job = db.query(models.JobInfo).filter(models.JobInfo.id == job_id).first()
   db.delete(del_job)
   db.commit()
