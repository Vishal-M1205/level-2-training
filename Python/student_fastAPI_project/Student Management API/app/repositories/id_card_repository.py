from app.database import get_connection
from app.schemas.id_card import IdCardCreate


async def upload_student_id_card(id_card: IdCardCreate):
    async with await get_connection() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute(
                """
INSERT INTO 
id_cards (student_id, original_filename, stored_filename, file_path)
VALUES
(
%s, %s, %s, %s
)
RETURNING id,student_id, original_filename, stored_filename, file_path;
""",
                (
                    id_card.student_id,
                    id_card.original_filename,
                    id_card.stored_filename,
                    id_card.file_path,
                ),
            )

            row = await cursor.fetchone()

            return row
