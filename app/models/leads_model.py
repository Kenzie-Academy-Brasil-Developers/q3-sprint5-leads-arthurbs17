from datetime import datetime
from app.configs.database import db

from sqlalchemy import Column, Integer, DateTime, String
from dataclasses import dataclass

@dataclass
class LeadsModel(db.Model):
    name: str
    email: str
    phone: str
    creation_date: datetime
    last_visit: datetime
    visits: int

    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    creation_date = Column(DateTime, default= datetime.utcnow())
    last_visit = Column(DateTime, default= datetime.utcnow())
    visits = Column(Integer, default=1)