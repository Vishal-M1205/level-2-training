from psycopg.errors import IntegrityError
from app.schemas.student import StudentCreate, StudentPatch, StudentUpdate
import app.repositories.student_repository as student_repository
from fastapi import HTTPException, UploadFile, status
import logging
from pathlib import Path
import aiofiles
from uuid import uuid4

logger = logging.getLogger(__name__)


async def upload_student_id_card(file: UploadFile):
    try:
        if file.size > (1024 * 1024) * 10:
            raise HTTPException(status_code=status.HTTP_413_CONTENT_TOO_LARGE)

        id_card_upload_directory = Path("uploads")

        Path.mkdir(id_card_upload_directory, parents=True, exist_ok=True)

        extension = Path(file.filename).suffix

        id_card_file_path = id_card_upload_directory / f"{uuid4()}.{extension}"

        async with aiofiles.open(id_card_file_path, "wb") as id_card_file:
            while chunk := await file.read(1024 * 1024):
                await id_card_file.write(chunk)

    except HTTPException:
        raise

    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def get_all_students(page: int, limit: int, **kwargs):
    try:
        query_params = {
            key: value for key, value in kwargs.items() if value is not None
        }
        offset = (page - 1) * limit
        return await student_repository.get_all_students(
            page, limit, offset, query_params
        )
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
