from sqlalchemy import Column, Integer, String
from backend.database import Base


class JobInfo(Base):
    __tablename__ = "job_bank"

    id = Column(Integer, primary_key=True, index=True)
    jobname = Column(String, unique=True)
    description = Column(String)
    location = Column(String, unique=True)
    applied  = Column(Integer)

