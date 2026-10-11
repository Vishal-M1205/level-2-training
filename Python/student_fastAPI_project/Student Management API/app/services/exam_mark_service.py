import logging
from psycopg.errors import IntegrityError
from fastapi import HTTPException

from app.schemas.exam_mark import ExamMarkCreate, ExamMarkPatch, ExamMarkUpdate
from app.repositories.exam_mark_repository import ExamMarkRepository


class ExamMarkService:

    def __init__(self, repository: ExamMarkRepository):
        self.logger = logging.getLogger(__name__)
        self.repository = repository

    async def get_all_exam_marks(self):
        try:
            return await self.repository.get_all_exam_marks()
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def get_exam_mark_by_id(self, exam_mark_id: int):
        try:
            exam_mark = await self.repository.get_exam_mark_by_id(exam_mark_id)
            if exam_mark is None:
                raise HTTPException(status_code=404, detail="Exam Mark Not Found")
            return exam_mark
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def create_exam_mark(self, exam_mark: ExamMarkCreate):
        try:
            return await self.repository.create_exam_mark(exam_mark)
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def update_exam_mark(self, exam_mark_id: int, exam_mark: ExamMarkUpdate):
        try:
            row = await self.repository.update_exam_mark(exam_mark_id, exam_mark)
            if row is None:
                raise HTTPException(status_code=404, detail="No Exam Mark Found")
            return row
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def delete_exam_mark(self, exam_mark_id: int):
        try:
            row = await self.repository.delete_exam_mark(exam_mark_id)
            if row is None:
                raise HTTPException(status_code=404, detail="No Exam Mark Found")
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def patch_exam_mark(self, exam_mark_id: int, exam_mark: ExamMarkPatch):
        try:
            payload = exam_mark.model_dump(exclude_unset=True)
            if payload == {}:
                raise HTTPException(
                    status_code=400,
                    detail="Bad Request : No fields provided for update",
                )
            row = await self.repository.patch_exam_mark(exam_mark_id, payload)
            if row is None:
                raise HTTPException(status_code=404, detail="No Exam Mark Found")
            return row
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

