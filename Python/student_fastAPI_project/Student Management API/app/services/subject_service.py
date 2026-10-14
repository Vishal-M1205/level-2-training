import logging
from psycopg.errors import IntegrityError
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.subject import SubjectCreate, SubjectPatch, SubjectUpdate
from app.repositories.subject_repository import SubjectRepository


class SubjectService:

    def __init__(self, repository: SubjectRepository, session: AsyncSession):
        self.logger = logging.getLogger(__name__)
        self.repository = repository
        self.session = session

    async def get_all_subjects(self):
        async with self.session.begin():
            try:
                return await self.repository.get_all_subjects()
            except IntegrityError:
                raise HTTPException(status_code=409, detail="Integrity Error")
            except Exception as e:
                self.logger.exception(e)
                raise HTTPException(status_code=500, detail="Internal Server Error")

    async def get_subject_by_id(self, subject_id: int):
        async with self.session.begin():
            try:
                subject = await self.repository.get_subject_by_id(subject_id)

                if subject is None:
                    raise HTTPException(status_code=404, detail="Subject Not Found")
                return subject
            except HTTPException:
                raise
            except IntegrityError:
                raise HTTPException(status_code=409, detail="Integrity Error")
            except Exception as e:
                self.logger.exception(e)
                raise HTTPException(status_code=500, detail="Internal Server Error")

    async def create_subject(self, subject: SubjectCreate):
        async with self.session.begin():
            try:
                return await self.repository.create_subject(subject)
            except HTTPException:
                raise
            except IntegrityError:
                raise HTTPException(status_code=409, detail="Integrity Error")
            except Exception as e:
                #! Always log and re-raise the error as Internal Server Error - 500
                self.logger.exception(e)
                raise HTTPException(status_code=500, detail="Internal Server Error")

    async def update_subject(self, subject_id: int, subject: SubjectUpdate):
        async with self.session.begin():
            try:
                row = await self.repository.update_subject(subject_id, subject)

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
                self.logger.exception(e)
                raise HTTPException(status_code=500, detail="Internal Server Error")

    async def delete_subject(self, subject_id: int):
        async with self.session.begin():
            try:
                row = await self.repository.delete_subject(subject_id)

                if row is None:
                    raise HTTPException(status_code=404, detail="No Subject Found")

            except HTTPException:
                raise
            except IntegrityError:
                raise HTTPException(status_code=409, detail="Integrity Error")
            except Exception as e:
                self.logger.exception(e)
                raise HTTPException(status_code=500, detail="Internal Server Error")

    async def patch_subject(self, subject_id: int, subject: SubjectPatch):
        async with self.session.begin():
            try:
                payload = subject.model_dump(exclude_unset=True)
                if payload == {}:
                    raise HTTPException(
                        status_code=400,
                        detail="Bad Request : No fields provided for update",
                    )
                row = await self.repository.patch_subject(subject_id, payload)
                if row is None:
                    raise HTTPException(status_code=404, detail="No Subject Found")
                return row
            except HTTPException:
                raise
            except IntegrityError:
                raise HTTPException(status_code=409, detail="Integrity Error")
            except Exception as e:
                self.logger.exception(e)
                raise HTTPException(status_code=500, detail="Internal Server Error")
