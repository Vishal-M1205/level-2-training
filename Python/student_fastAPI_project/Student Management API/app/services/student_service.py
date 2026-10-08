from psycopg.errors import IntegrityError
from app.schemas.student import StudentCreate, StudentPatch, StudentUpdate
import app.repositories.student_repository as student_repository
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)


async def get_all_students(**kwargs):
    try:
        params = {key: value for key, value in kwargs.items() if value is not None}

        return await student_repository.get_all_students(params)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def get_student_by_id(student_id: int):
    try:
        student = await student_repository.get_student_by_id(student_id)

        if student is None:
            raise HTTPException(status_code=404, detail="Student Not Found")
        return student
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def create_student(student: StudentCreate):
    try:
        return await student_repository.create_student(student)
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        #! Always log and re-raise the error as Internal Server Error - 500
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def update_student(student_id: int, student: StudentUpdate):
    try:
        row = await student_repository.update_student(student_id, student)

        #! Checking the row because student data need to be there to update
        #! If no data found in that ID , None is returned (fetchone)
        if row is None:
            raise HTTPException(status_code=404, detail="No Student Found")

        return row
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def delete_student(student_id: int):
    try:
        row = await student_repository.delete_student(student_id)

        if row is None:
            raise HTTPException(status_code=404, detail="No Student Found")

    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def patch_student(student_id: int, student: StudentPatch):
    try:
        payload = student.model_dump(exclude_unset=True)
        if payload == {}:
            raise HTTPException(
                status_code=400, detail="Bad Request : No fields provided for update"
            )
        row = await student_repository.patch_student(student_id, payload)
        if row is None:
            raise HTTPException(status_code=404, detail="No Student Found")
        return row
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
