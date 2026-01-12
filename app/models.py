from sqlalchemy import Column, Integer, String, Date, Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String) 


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(String)
    responsibilities = Column(String)
    join_date = Column(Date)
    exit_date = Column(Date, nullable=True)
    active = Column(Boolean, default=True)
