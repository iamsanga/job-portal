from typing import List
from pydantic import BaseModel


class JobInfoBase(BaseModel):
    jobname: str
    description: str
    location : str

class JobInfo(JobInfoBase):
    id: int

    class Config:
        orm_mode = True

class JobReceived(JobInfo):
    applied: int
    class Config:
        orm_mode = True
