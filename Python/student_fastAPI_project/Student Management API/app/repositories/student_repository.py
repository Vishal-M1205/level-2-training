from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
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

        for field, values in params.items():
            query = query.where(getattr(Student, field) == values)

        query = query.limit(limit).offset(offset)

        rows = await self.session.execute(query)
        rows = rows.scalars().all()

        query = select(func.count()).select_from(Student)

        for field, values in params.items():
            query = query.where(getattr(Student, field) == values)

        total_records = await self.session.execute(query)
        total_records = total_records.scalar()

        total_pages = math.ceil(total_records / limit)

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
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
    INSERT INTO 
    students (name,age,gender)
    VALUES 
    (%s,%s,%s) 
    RETURNING id,name,age,gender; 
    """,  #! RETURNING - fetches the row added
                (student.name, student.age, student.gender),
                #!ANOTHER WAY : tuple( student.model_dump().values() ),   object -> dict -> dict.values() -> tuple
            )

            row = await cursor.fetchone()

            return row

    async def update_student(self, student_id: int, student: StudentUpdate):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
    UPDATE students 
    SET 
    name = %s,
    age = %s,
    gender = %s
    WHERE 
    id = %s
    RETURNING id, name, age, gender; 
    """,
                (student.name, student.age, student.gender, student_id),
            )

            row = await cursor.fetchone()

            return row

    async def delete_student(self, student_id: int):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
    DELETE 
    FROM students 
    WHERE 
    id = %s
    RETURNING id;
    """,  #! If the student exist and deleted RETURNING will return the 'id'
                #! No student found then None
                (student_id,),
            )

            row = await cursor.fetchone()

            return row

    async def patch_student(self, student_id: int, payload: dict):
        values = tuple(payload.values())

        query = self.util.generate_query(payload, ",")

        async with self.connection.cursor() as cursor:
            await cursor.execute(
                f"""
    UPDATE students
    SET 
    {query}
    WHERE 
    id = %s
    RETURNING id,name,age,gender;
    """,
                (*values, student_id),
            )

            row = await cursor.fetchone()

            return row
