from app.database import get_connection
from app.schemas.student import StudentCreate, StudentUpdate


async def get_all_students(params: dict):
    query = ""
    values = []
    if params != {}:
        fields = list(params.keys())
        values = list(params.values())

        query = [f"{x} = %s" for x in fields]
        query = " AND ".join(query)
        query = "WHERE " + query

    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(
                f"""
  SELECT 
  id,
  name,
  age,
  gender 
  FROM students
  {query}
""",
                values,
            )
            rows = await cursor.fetchall()
            return rows


async def get_student_by_id(student_id: int):
    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
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


async def create_student(student: StudentCreate):
    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
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


async def update_student(student_id: int, student: StudentUpdate):
    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
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


async def delete_student(student_id: int):
    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
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


async def patch_student(student_id: int, payload: dict):
    fields = list(payload.keys())
    values = tuple(payload.values())

    query = [f"{x} = %s" for x in fields]

    query = ",".join(query)

    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
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
