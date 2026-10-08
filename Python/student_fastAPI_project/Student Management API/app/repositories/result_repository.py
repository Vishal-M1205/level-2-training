from app.database import get_connection


async def get_student_exam_result_by_id(student_id: int):
    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(
                """
SELECT 
st.id,
st.name as student_name,
sub.name as subject_name,
ex.mark 
FROM exam_marks ex 
JOIN students st 
ON st.id = ex.student_id
JOIN subjects sub
ON sub.id = ex.subject_id 
WHERE 
st.id = %s;
""",
                (student_id,),
            )

            rows = await cursor.fetchall()

            return rows
