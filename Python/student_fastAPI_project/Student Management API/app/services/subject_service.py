from psycopg.errors import IntegrityError
from app.schemas.subject import SubjectCreate, SubjectPatch, SubjectUpdate
import app.repositories.subject_repository as subject_repository
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)


async def get_all_subjects():
    try:
        return await subject_repository.get_all_subjects()
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def get_subject_by_id(subject_id: int):
    try:
        subject = await subject_repository.get_subject_by_id(subject_id)

        if subject is None:
            raise HTTPException(status_code=404, detail="Subject Not Found")
        return subject
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def create_subject(subject: SubjectCreate):
    try:
        return await subject_repository.create_subject(subject)
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        #! Always log and re-raise the error as Internal Server Error - 500
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def update_subject(subject_id: int, subject: SubjectUpdate):
    try:
        row = await subject_repository.update_subject(subject_id, subject)

        #! Checking the row because subject data need to be there to update
        #! If no data found in that ID , None is returned (fetchone)
        if row is None:
            raise HTTPException(status_code=404, detail="No Subject Found")

        return row
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def delete_subject(subject_id: int):
    try:
        row = await subject_repository.delete_subject(subject_id)

        if row is None:
            raise HTTPException(status_code=404, detail="No Subject Found")

    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def patch_subject(subject_id: int, subject: SubjectPatch):
    try:
        payload = subject.model_dump(exclude_unset=True)
        if payload == {}:
            raise HTTPException(
                status_code=400, detail="Bad Request : No fields provided for update"
            )
        print(payload)
        row = await subject_repository.patch_subject(subject_id, payload)
        if row is None:
            raise HTTPException(status_code=404, detail="No Subject Found")
        return row
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")




