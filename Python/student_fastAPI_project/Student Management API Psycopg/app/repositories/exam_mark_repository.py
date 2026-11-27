from psycopg import AsyncConnection
from app.schemas.exam_mark import ExamMarkCreate, ExamMarkUpdate


class ExamMarkRepository:

    def __init__(self, connection: AsyncConnection):
        self.connection = connection

    async def get_all_exam_marks(self):
        async with self.connection.cursor() as cursor:
            await cursor.execute("""
SELECT 
id,
student_id,
subject_id,
mark
FROM 
exam_marks
""")
            rows = await cursor.fetchall()
            return rows

    async def get_exam_mark_by_id(self, exam_mark_id: int):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
SELECT 
id,
student_id,
subject_id,
mark 
FROM 
exam_marks
WHERE id = %s
""",
                (exam_mark_id,),
            )
            row = await cursor.fetchone()
            return row

    async def create_exam_mark(self, exam_mark: ExamMarkCreate):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
INSERT INTO 
exam_marks (student_id, subject_id, mark)
VALUES 
(%s, %s, %s) 
RETURNING id, student_id, subject_id, mark; 
""",
                (exam_mark.student_id, exam_mark.subject_id, exam_mark.mark),
            )
            row = await cursor.fetchone()
            return row

    async def update_exam_mark(self, exam_mark_id: int, exam_mark: ExamMarkUpdate):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
UPDATE exam_marks 
SET 
student_id = %s,
subject_id = %s,
mark = %s
WHERE 
id = %s
RETURNING id, student_id, subject_id, mark; 
""",
                (exam_mark.student_id, exam_mark.subject_id, exam_mark.mark, exam_mark_id),
            )
            row = await cursor.fetchone()
            return row

    async def delete_exam_mark(self, exam_mark_id: int):
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
DELETE 
FROM exam_marks 
WHERE 
id = %s
RETURNING id;
""",
                (exam_mark_id,),
            )
            row = await cursor.fetchone()
            return row

    async def patch_exam_mark(self, exam_mark_id: int, payload: dict):
        fields = list(payload.keys())
        values = tuple(payload.values())

        query = [f"{x} = %s" for x in fields]
        query = ",".join(query)

        async with self.connection.cursor() as cursor:
            await cursor.execute(
                f"""
UPDATE exam_marks
SET 
{query}
WHERE 
id = %s
RETURNING id, student_id, subject_id, mark;
""",
                (*values, exam_mark_id),
            )
            row = await cursor.fetchone()
            return row
