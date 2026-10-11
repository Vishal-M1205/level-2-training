from psycopg.errors import IntegrityError
from app.repositories.result_repository import ExamResultRepository
from fastapi import HTTPException
from decimal import Decimal
import logging


class ExamResultService:

    def __init__(self, repository: ExamResultRepository):
        self.logger = logging.getLogger(__name__)
        self.repository = repository

    async def get_student_exam_result_by_id(self, student_id: int) -> dict:
        try:
            marks = await self.repository.get_student_exam_result_by_id(student_id)
            if marks == []:
                raise HTTPException(
                    status_code=404,
                    detail=f"No Result Found for the Student ID : {student_id} ",
                )
            total = sum(x["mark"] for x in marks)
            grade = self.calculate_grade_from_total(total)

            return {
                "student_id": student_id,
                "student_name": marks[0]["student_name"],
                "subjects": [
                    {"subject_name": x["subject_name"], "mark": x["mark"]}
                    for x in marks
                ],
                "total": total,
                "grade": grade,
            }

        except HTTPException:
            raise
        except IntegrityError:
            raise HTTPException(status_code=409, detail="Integrity Error")
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")

    def calculate_grade_from_total(self, total: Decimal) -> str:
        match total:
            case total if total > 450:
                return "A"
            case total if total > 400:
                return "B"
            case total if total > 350:
                return "C"
            case _:
                return "F"
