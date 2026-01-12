from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from ..database import SessionLocal
from ..models import Employee
from ..schemas import EmployeeCreate
from ..dependencies import admin_only

router = APIRouter(prefix="/employees")

@router.post("/", dependencies=[Depends(admin_only)])
def onboard_employee(data: EmployeeCreate):
    db = SessionLocal()
    emp = Employee(**data.dict())
    db.add(emp)
    db.commit()
    return {"msg": "Employee onboarded"}

@router.get("/")
def list_employees():
    db = SessionLocal()
    return db.query(Employee).all()

@router.post("/offboard/{emp_id}", dependencies=[Depends(admin_only)])
def offboard_employee(emp_id: int):
    db = SessionLocal()
    emp = db.query(Employee).get(emp_id)
    emp.active = False
    emp.exit_date = date.today()
    db.commit()
    return {"msg": "Employee offboarded"}
