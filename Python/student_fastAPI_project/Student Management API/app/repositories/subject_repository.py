from psycopg import AsyncConnection
from app.schemas.subject import SubjectCreate, SubjectUpdate

"""
Why await in get_connection() - as it invlove in I/O operation - connecting to DB
connection.cursor() is just returning the coroutine curo object so no await needed
"""


class SubjectRepository:

    def __init__(self, connection: AsyncConnection):
        self.connection = connection

    async def get_all_subjects(self):
        async with self.connection.cursor() as cursor:
            await cursor.execute("""
SELECT
id,  
name
FROM
subjects;
""")

            rows = await cursor.fetchall()

            return rows

    async def get_subject_by_id(self, subject_id: int):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
SELECT 
id,
name 
FROM 
subjects
WHERE 
id = %s
""",
                (subject_id,),
            )

            row = await cursor.fetchone()

            return row

    async def create_subject(self, subject: SubjectCreate):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
INSERT INTO
subjects (name)
VALUES 
(%s)
RETURNING id, name;
""",
                (subject.name,),
            )

            row = await cursor.fetchone()

            return row

    async def update_subject(self, subject_id: int, subject: SubjectUpdate):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
UPDATE subjects
SET
name = %s
WHERE 
id = %s
RETURNING id,name;
""",
                (subject.name, subject_id),
            )

            row = await cursor.fetchone()

            return row

    async def patch_subject(self, subject_id: int, payload: dict):
        fields = list(payload.keys())
        values = tuple(payload.values())

        query = [f"{x} = %s" for x in fields]

        query = ",".join(query)

        async with self.connection.cursor() as cursor:
            await cursor.execute(
                f"""
UPDATE subjects
SET 
{query}
WHERE 
id = %s
RETURNING id,name;
""",
                (*values, subject_id),
            )

            row = await cursor.fetchone()

            return row

    async def delete_subject(self, subject_id: int):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
DELETE 
FROM subjects 
WHERE 
id = %s
RETURNING id;
""",  #! If the student exist and deleted RETURNING will return the 'id'
                #! No student found then None
                (subject_id,),
            )

            row = await cursor.fetchone()

            return row



