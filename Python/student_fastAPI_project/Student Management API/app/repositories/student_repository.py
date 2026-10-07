from app.database import get_connection
from app.models.student import StudentCreate, StudentUpdate


def get_all_students():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
  SELECT 
  id,
  name,
  age,
  gender 
  FROM students
""")
            rows = cursor.fetchall()  #! if no records found fetchall return [] not None
            return rows


def get_student_by_id(student_id: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
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
            row = cursor.fetchone()  #! fetchone return None
            return row


"""
In the create_student , no need for connection.commit()/rollback()
because the contextmanage will call rollback on exception
and commit() on exit of the context

"""


def create_student(student: StudentCreate):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
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

            row = cursor.fetchone()

            return row


def update_student(student_id: int, student: StudentUpdate):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
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

            row = cursor.fetchone()

            return row


def delete_student(student_id: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
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

            row = cursor.fetchone()

            return row


def patch_student(student_id: int, payload: dict):
    fields = list(payload.keys())
    values = tuple(payload.values())

    query = [f"{x} = %s" for x in fields]

    query = ",".join(query)

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                f"""
UPDATE students
SET 
{query}
WHERE 
id = %s
""",
                (*values, student_id),
            )

            row = cursor.fetchone()

            return row
