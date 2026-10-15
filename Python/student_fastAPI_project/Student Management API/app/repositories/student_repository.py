from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, insert, update, delete
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate
from app.utils.query_utils import QueryUtil
import math


class StudentRepository:

    def __init__(self, util: QueryUtil, session: AsyncSession):
        self.util = util
        self.session = session

    async def get_all_students(self, page: int, limit: int, offset: int, params: dict):
        query = select(Student)

        for field, value in params.items():
            if field == "name":
                query = query.where(getattr(Student, field).ilike(f"%{value}%"))
            else:
                query = query.where(getattr(Student, field) == value)

        query = query.limit(limit).offset(offset)

        rows = await self.session.execute(query)
        rows = rows.scalars().all()

        query = select(func.count()).select_from(Student)

        for field, values in params.items():
            query = query.where(getattr(Student, field) == values)

        total_records = await self.session.execute(query)
        total_records = total_records.scalar()

        total_pages = math.ceil(total_records / limit) or 1

        return {
            "students": rows,
            "total": total_records,
            "page": page,
            "limit": limit,
            "total_pages": total_pages,
        }

    async def get_student_by_id(self, student_id: int):
        row = await self.session.get(Student, student_id)
        return row

    """
    In the create_student , no need for connection.commit()/rollback()
    because the contextmanage will call rollback on exception
    and commit() on exit of the context

    """

    async def create_student(self, student: StudentCreate):
        stmnt = insert(Student).values(**student.model_dump()).returning(Student)

        row = await self.session.execute(stmnt)
        row = row.scalar_one()

        return row

    async def update_student(self, student_id: int, student: StudentUpdate):
        stmnt = (
            update(Student)
            .where(Student.id == student_id)
            .values(**student.model_dump())
            .returning(Student)
        )

        row = await self.session.execute(stmnt)
        row = row.scalar_one()

        return row

    async def delete_student(self, student_id: int):
        stmnt = delete(Student).where(Student.id == student_id).returning(Student.id)

        row = await self.session.execute(stmnt)
        row = row.scalar_one()

        print(row)

        return row

    async def patch_student(self, student_id: int, payload: dict):
        stmnt = (
            update(Student)
            .where(Student.id == student_id)
            .values(**payload)
            .returning(Student)
        )

        row = await self.session.execute(stmnt)
        row = row.scalar_one()

        return row
