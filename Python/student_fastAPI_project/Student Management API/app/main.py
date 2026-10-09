from fastapi import FastAPI, Response

from app.utils.log import setup_logging
from app.routes.student_routes import router as student_router
from app.routes.subject_routes import router as subject_router
from app.routes.exam_mark_routes import router as exam_mark_router

from app.core.config import config

import logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=config.app_name,
    description="Connected with Postgres and handles CRUD operations",
    version=config.app_version,
)
# ! returns a FastAPI object to initiate the application

app.include_router(student_router)
app.include_router(subject_router)
app.include_router(exam_mark_router)


@app.get("/", tags=["Home Page"])
def home(response: Response):
    """Root endpoint value is returned"""
    response.set_cookie(key="theme", value="dark", secure=False, httponly=True)
    #! If the secure is true the browser send the cookie data in HTTPS , for False -> HTTP
    #! For preventing JS API like cookie to access the data
    return {"title": config.app_name}


"""Creating a /students end point of GET to take data from the db"""
