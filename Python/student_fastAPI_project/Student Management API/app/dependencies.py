from typing import Annotated
from app.database import get_db_connection
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

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

DB_Session = Annotated[AsyncSession, Depends(get_db_connection)]


def get_exam_result_repository(
    session: DB_Session,
) -> ExamResultRepository:
    return ExamResultRepository(session)


def get_exam_result_service(
    repository: Annotated[ExamResultRepository, Depends(get_exam_result_repository)],
) -> ExamResultService:
    return ExamResultService(repository)


def get_student_repository(
    util: Annotated[QueryUtil, Depends(QueryUtil)], session: DB_Session
) -> StudentRepository:
    return StudentRepository(util, session)


def get_student_service(
    repository: Annotated[StudentRepository, Depends(get_student_repository)],
    session: DB_Session,
) -> StudentService:
    return StudentService(repository, session)


def get_id_card_repository(
    session: DB_Session,
) -> IdCardRepository:
    return IdCardRepository(session)


def get_id_card_service(
    repository: Annotated[IdCardRepository, Depends(get_id_card_repository)],
) -> IdCardService:
    return IdCardService(repository)


def get_subject_repository(
    session: DB_Session,
) -> SubjectRepository:
    return SubjectRepository(session)


def get_subject_service(
    repository: Annotated[SubjectRepository, Depends(get_subject_repository)],
    session: DB_Session,
) -> SubjectService:
    return SubjectService(repository, session)


def get_exam_mark_repository(
    session: DB_Session,
) -> ExamMarkRepository:
    return ExamMarkRepository(session)


def get_exam_mark_service(
    repository: Annotated[ExamMarkRepository, Depends(get_exam_mark_repository)],
    session: DB_Session,
) -> ExamMarkService:
    return ExamMarkService(repository, session)
