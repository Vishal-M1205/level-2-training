from app.models.student import StudentCreate, StudentPatch, StudentUpdate
import app.repositories.student_repository as student_repository
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)


def get_all_students():
    try:
        return student_repository.get_all_students()
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


def get_student_by_id(student_id: int):
    try:
        student = student_repository.get_student_by_id(student_id)

        if student is None:
            raise HTTPException(status_code=404, detail="Student Not Found")
        return student
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


def create_student(student: StudentCreate):
    try:
        return student_repository.create_student(student)
    except HTTPException:
        raise
    except Exception as e:
        #! Always log and re-raise the error as Internal Server Error - 500
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


def update_student(student_id: int, student: StudentUpdate):
    try:
        row = student_repository.update_student(student_id, student)

        #! Checking the row because student data need to be there to update
        #! If no data found in that ID , None is returned (fetchone)
        if row is None:
            raise HTTPException(status_code=404, detail="No Student Found")

        return row
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


def delete_student(student_id: int):
    try:
        row = student_repository.delete_student(student_id)

        if row is None:
            raise HTTPException(status_code=404, detail="No Student Found")

    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


def patch_student(student_id: int, student: StudentPatch):
    try:
        payload = student.model_dump(exclude_unset=True)
        return student_repository.patch_student(student_id, payload)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
