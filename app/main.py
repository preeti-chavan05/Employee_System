from fastapi import FastAPI
from .database import Base, engine
from .routers import auth_router, employee_router
from .models import User, Employee

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tech Prescient Employee System")

app.include_router(auth_router.router)
app.include_router(employee_router.router)


