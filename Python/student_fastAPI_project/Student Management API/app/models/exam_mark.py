from app.models.base import Base
from sqlalchemy import Integer, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.subject import Subject
    from app.models.student import Student


class ExamMark(Base):
    __tablename__ = "exam_marks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id"))
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))
    mark: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)

    subject: Mapped["Subject"] = relationship(back_populates="exam_marks")
    student: Mapped["Student"] = relationship(back_populates="exam_marks")
