from psycopg.errors import IntegrityError, UniqueViolation
from app.schemas.student import StudentCreate, StudentPatch, StudentUpdate
from app.schemas.id_card import IdCardCreate
import app.repositories.student_repository as student_repository
import app.repositories.id_card_repository as id_card_repository
from fastapi import HTTPException, UploadFile, status, Cookie
from app.utils.path_utils import generate_file_path
from pathlib import Path
import logging
import aiofiles

logger = logging.getLogger(__name__)


async def upload_student_id_card(student_id: int, file: UploadFile):
    try:
        if file.size > (1024 * 1024) * 10:
            raise HTTPException(status_code=status.HTTP_413_CONTENT_TOO_LARGE)

        id_card_file_path = generate_file_path(file, "uploads")

        stored_filename = Path(id_card_file_path).name

        async with aiofiles.open(id_card_file_path, "wb") as id_card_file:
            while chunk := await file.read(1024 * 1024):
                await id_card_file.write(chunk)

        id_card_payload = IdCardCreate.model_validate(
            {
                "student_id": student_id,
                "original_filename": file.filename,
                "stored_filename": stored_filename,
                "file_path": str(id_card_file_path),
            }
        )

        id_card = await id_card_repository.upload_student_id_card(id_card_payload)

        if id_card is None:
            raise HTTPException(status_code=404, detail="ID Card Not Found")

        return id_card

    except UniqueViolation:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="ID Card Already Found"
        )

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
