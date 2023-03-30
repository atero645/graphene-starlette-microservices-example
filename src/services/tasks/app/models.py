from . import db
from sqlalchemy import Column, Integer, String

class Task(db.Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    status = Column(String)
