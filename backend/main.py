from typing import List

import uvicorn, logging
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend  import models, schemas, crud
from backend.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/jobs", response_model=List[schemas.JobInfo])
def read_jobs(db: Session = Depends(get_db)):
    return crud.read_jobs(db)

@app.get("/jobs/received", response_model=List[schemas.JobReceived])
def received_jobs(db: Session = Depends(get_db)):
    return crud.received_jobs(db)


@app.post("/jobs", response_model=schemas.JobInfo)
def create_job(job: schemas.JobInfoBase, db: Session = Depends(get_db)):

    return crud.create_job(db=db, job=job)

@app.put("/jobs/apply/{job_id}")
def apply_job(job_id:int,db: Session = Depends(get_db)):
    try:
        crud.apply_job(db,job_id)
        return {"detail": "Applied"}
    except:
        return {"detail" : "Apply failed"}


@app.put("/jobs/{job_id}", response_model=schemas.JobInfo)
def update_job(job_id:int,job: schemas.JobInfoBase, db: Session = Depends(get_db)):

    return crud.update_job(db,job_id,job)

@app.delete("/jobs/{job_id}")
def delete_job(job_id:int, db: Session = Depends(get_db)):
    crud.delete_job(db, job_id)
    return {"detail": "Job deleted successfully"}

if __name__ == "__main__":
  uvicorn.run(app, host="127.0.0.1", port=8081,log_level=logging.DEBUG,
  log_config=logging.basicConfig(filename='backend/logs/backend_server.log',
    filemode='a+',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'))
