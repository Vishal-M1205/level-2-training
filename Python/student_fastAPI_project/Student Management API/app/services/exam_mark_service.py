from psycopg.errors import IntegrityError
from app.schemas.exam_mark import ExamMarkCreate, ExamMarkPatch, ExamMarkUpdate
import app.repositories.exam_mark_repository as exam_mark_repository
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)


async def get_all_exam_marks():
    try:
        return await exam_mark_repository.get_all_exam_marks()
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def get_exam_mark_by_id(exam_mark_id: int):
    try:
        exam_mark = await exam_mark_repository.get_exam_mark_by_id(exam_mark_id)
        if exam_mark is None:
            raise HTTPException(status_code=404, detail="Exam Mark Not Found")
        return exam_mark
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def create_exam_mark(exam_mark: ExamMarkCreate):
    try:
        return await exam_mark_repository.create_exam_mark(exam_mark)
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def update_exam_mark(exam_mark_id: int, exam_mark: ExamMarkUpdate):
    try:
        row = await exam_mark_repository.update_exam_mark(exam_mark_id, exam_mark)
        if row is None:
            raise HTTPException(status_code=404, detail="No Exam Mark Found")
        return row
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def delete_exam_mark(exam_mark_id: int):
    try:
        row = await exam_mark_repository.delete_exam_mark(exam_mark_id)
        if row is None:
            raise HTTPException(status_code=404, detail="No Exam Mark Found")
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def patch_exam_mark(exam_mark_id: int, exam_mark: ExamMarkPatch):
    try:
        payload = exam_mark.model_dump(exclude_unset=True)
        if payload == {}:
            raise HTTPException(
                status_code=400, detail="Bad Request : No fields provided for update"
            )
        row = await exam_mark_repository.patch_exam_mark(exam_mark_id, payload)
        if row is None:
            raise HTTPException(status_code=404, detail="No Exam Mark Found")
        return row
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

