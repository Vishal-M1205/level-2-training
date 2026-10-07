from fastapi import FastAPI
from app.utils.log import setup_logging
from app.routes.student_routes import router as student_router
import logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()
# ! returns a FastAPI object to initiate the application

app.include_router(student_router)


@app.get("/")
def home():
    """Root endpoint value is returned"""
    return {"title": "Student Management System"}


"""Creating a /students end point of GET to take data from the db"""
