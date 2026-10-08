from psycopg.errors import IntegrityError
import app.repositories.result_repository as result_repository
from fastapi import HTTPException
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)


async def get_student_exam_result_by_id(student_id: int) -> dict:
    try:
        marks = await result_repository.get_student_exam_result_by_id(student_id)
        if marks == []:
            raise HTTPException(
                status_code=404,
                detail=f"No Result Found for the Student ID : {student_id} ",
            )
        total = sum(x["mark"] for x in marks)
        grade = calculate_grade_from_total(total)

        return {
            "student_id": student_id,
            "student_name": marks[0]["student_name"],
            "subjects": [
                {"subject_name": x["subject_name"], "mark": x["mark"]} for x in marks
            ],
            "total": total,
            "grade": grade,
        }

    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Integrity Error")
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


def calculate_grade_from_total(total: Decimal) -> str:
    match total:
        case total if total > 450:
            return "A"
        case total if total > 400:
            return "B"
        case total if total > 350:
            return "C"
        case _:
            return "F"

