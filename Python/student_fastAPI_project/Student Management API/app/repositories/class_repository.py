from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.exam_mark import ExamMark
from app.models.student import Student


class ClassRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_top_five_students(self):
        stmnt = (
            select(Student.id, Student.name, func.sum(ExamMark.mark).label("total"))
            .join(ExamMark, Student.id == ExamMark.student_id)
            .group_by(Student.id, Student.name)
            .order_by(func.sum(ExamMark.mark))
            .limit(5)
        )

        rows = await self.session.execute(stmnt)

        return {"students": rows.mappings().all()}
