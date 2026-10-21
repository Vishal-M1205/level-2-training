from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from app.interfaces.id_card_interface import IdCardInterface
from app.models.id_card import IdCard
from app.schemas.id_card import IdCardCreate


class IdCardRepository(IdCardInterface):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def upload_student_id_card(self, id_card: IdCardCreate):
        stmnt = insert(IdCard).values(**id_card.model_dump()).returning(IdCard)

        row = await self.session.execute(stmnt)
        row = row.scalar_one()

        return row
