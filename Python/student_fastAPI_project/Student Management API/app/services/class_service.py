from app.repositories.class_repository import ClassRepository
from sqlalchemy.ext.asyncio import AsyncSession


class ClassService:
    def __init__(self, repository: ClassRepository, session: AsyncSession):
        self.repository = repository
        self.session = session

    async def get_top_five_students(self):
        async with self.session.begin():
            return await self.repository.get_top_five_students()
