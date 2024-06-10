from fastapi import FastAPI
from .database import engine
from . import models
from .routers import project, data, status, alarm ,machine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(project.router, prefix="/projects", tags=["projects"])
app.include_router(data.router, prefix="/data", tags=["data"])
app.include_router(status.router, prefix="/status", tags=["status"])
app.include_router(alarm.router, prefix="/alarms", tags=["alarms"])
app.include_router(machine.router, prefix="/machines", tags=["machines"])

origins = [
    "http://localhost:3000",  
    "http://localhost:8000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)