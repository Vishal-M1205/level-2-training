from psycopg.errors import IntegrityError, UniqueViolation
from app.schemas.student import StudentCreate, StudentPatch, StudentUpdate
from app.schemas.id_card import IdCardCreate
from app.repositories.student_repository import StudentRepository
from fastapi import HTTPException, status, Cookie
from app.core.types import StudentID
import logging


class StudentService:
    def __init__(self, repository: StudentRepository):
        self.logger = logging.getLogger(__name__)
        self.repository = repository

    async def get_all_students(self, page: int, limit: int, **kwargs):
        try:
            query_params = {
                key: value for key, value in kwargs.items() if value is not None
            }
            offset = (page - 1) * limit
            return await self.repository.get_all_students(
                page, limit, offset, query_params
            )
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def get_student_by_id(self, student_id: StudentID):
        try:

            student = await self.repository.get_student_by_id(student_id)

            if student is None:
                raise HTTPException(status_code=404, detail="Student Not Found")
            return student
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def create_student(self, student: StudentCreate):
        try:
            return await self.repository.create_student(student)
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            #! Always log and re-raise the error as Internal Server Error - 500
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def update_student(self, student_id: int, student: StudentUpdate):
        try:
            row = await self.repository.update_student(student_id, student)

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
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def delete_student(self, student_id: int):
        try:
            row = await self.repository.delete_student(student_id)

            if row is None:
                raise HTTPException(status_code=404, detail="No Student Found")

        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def patch_student(self, student_id: int, student: StudentPatch):
        try:
            payload = student.model_dump(exclude_unset=True)
            if payload == {}:
                raise HTTPException(
                    status_code=400,
                    detail="Bad Request : No fields provided for update",
                )
            row = await self.repository.patch_student(student_id, payload)
            if row is None:
                raise HTTPException(status_code=404, detail="No Student Found")
            return row
        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
