from typing import Annotated
from app.database import get_db_connection
from fastapi import Depends
from psycopg import AsyncConnection

from app.repositories.student_repository import StudentRepository
from app.repositories.id_card_repository import IdCardRepository
from app.repositories.result_repository import ExamResultRepository
from app.repositories.subject_repository import SubjectRepository
from app.repositories.exam_mark_repository import ExamMarkRepository
from app.services.result_service import ExamResultService
from app.services.student_service import StudentService
from app.services.id_card_service import IdCardService
from app.services.subject_service import SubjectService
from app.services.exam_mark_service import ExamMarkService
from app.utils.query_utils import QueryUtil

DB_Connection = Annotated[AsyncConnection, Depends(get_db_connection)]


def get_exam_result_repository(
    connection: DB_Connection,
) -> ExamResultRepository:
    return ExamResultRepository(connection)


def get_exam_result_service(
    repository: Annotated[ExamResultRepository, Depends(get_exam_result_repository)],
) -> ExamResultService:
    return ExamResultService(repository)


def get_student_repository(
    util: Annotated[QueryUtil, Depends(QueryUtil)], connection: DB_Connection
) -> StudentRepository:
    return StudentRepository(util, connection)


def get_student_service(
    repository: Annotated[StudentRepository, Depends(get_student_repository)],
) -> StudentService:
    return StudentService(repository)


def get_id_card_repository(
    connection: DB_Connection,
) -> IdCardRepository:
    return IdCardRepository(connection)


def get_id_card_service(
    repository: Annotated[IdCardRepository, Depends(get_id_card_repository)],
) -> IdCardService:
    return IdCardService(repository)


def get_subject_repository(
    connection: DB_Connection,
) -> SubjectRepository:
    return SubjectRepository(connection)


def get_subject_service(
    repository: Annotated[SubjectRepository, Depends(get_subject_repository)],
) -> SubjectService:
    return SubjectService(repository)


def get_exam_mark_repository(
    connection: DB_Connection,
) -> ExamMarkRepository:
    return ExamMarkRepository(connection)


def get_exam_mark_service(
    repository: Annotated[ExamMarkRepository, Depends(get_exam_mark_repository)],
) -> ExamMarkService:
    return ExamMarkService(repository)
