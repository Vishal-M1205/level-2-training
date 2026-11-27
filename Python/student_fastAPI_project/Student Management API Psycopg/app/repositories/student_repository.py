from psycopg import AsyncConnection

from app.schemas.student import StudentCreate, StudentUpdate
from app.utils.query_utils import QueryUtil
import math


class StudentRepository:

    def __init__(self, util: QueryUtil, connection: AsyncConnection):
        self.util = util
        self.connection = connection

    async def get_all_students(self, page: int, limit: int, offset: int, params: dict):
        query = ""
        values = []
        pagination = "LIMIT %s OFFSET %s"
        if params != {}:
            values = tuple(params.values())
            query = "WHERE " + self.util.generate_query(params, " AND ")

        async with self.connection.cursor() as cursor:
            await cursor.execute(
                f"""
    SELECT 
    id,
    name,
    age,
    gender 
    FROM students
    {query}
    {pagination}
    
    """,
                (*values, limit, offset),
            )
            rows = await cursor.fetchall()

            await cursor.execute("""
    SELECT 
    COUNT(*) as total_records 
    FROM students
    """)
            total = await cursor.fetchone()
            total_records = total["total_records"]
            total_pages = math.ceil(total_records / limit)

            return {
                "students": rows,
                "total": total_records,
                "page": page,
                "limit": limit,
                "total_pages": total_pages,
            }

    async def get_student_by_id(self, student_id: int):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
    SELECT 
    id,
    name,
    age,
    gender 
    FROM students
    WHERE id = %s
    """,
                (student_id,),
            )
            row = await cursor.fetchone()  #! fetchone return None
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
