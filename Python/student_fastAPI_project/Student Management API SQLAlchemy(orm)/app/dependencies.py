from typing import Annotated
from app.database import get_db_connection
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.interfaces.class_interface import ClassInterface
from app.interfaces.result_interface import ExamResultInterface
from app.interfaces.id_card_interface import IdCardInterface
from app.interfaces.subject_interface import SubjectInterface
from app.interfaces.student_interface import StudentInterface
from app.repositories.class_repository import ClassRepository
from app.repositories.student_repository import StudentRepository
from app.repositories.id_card_repository import IdCardRepository
from app.repositories.result_repository import ExamResultRepository
from app.repositories.subject_repository import SubjectRepository
from app.repositories.exam_mark_repository import ExamMarkRepository
from app.services.class_service import ClassService
from app.services.result_service import ExamResultService
from app.services.student_service import StudentService
from app.services.id_card_service import IdCardService
from app.services.subject_service import SubjectService
from app.services.exam_mark_service import ExamMarkService

DB_Session = Annotated[AsyncSession, Depends(get_db_connection)]


def get_exam_result_repository(
    session: DB_Session,
) -> ExamResultInterface:
    return ExamResultRepository(session)


def get_exam_result_service(
    repository: Annotated[ExamResultInterface, Depends(get_exam_result_repository)],
    session: DB_Session,
) -> ExamResultService:
    return ExamResultService(repository, session)


def get_student_repository(session: DB_Session) -> StudentInterface:
    return StudentRepository(session)


def get_student_service(
    repository: Annotated[StudentInterface, Depends(get_student_repository)],
    session: DB_Session,
) -> StudentService:
    return StudentService(repository, session)


def get_id_card_repository(
    session: DB_Session,
) -> IdCardInterface:
    return IdCardRepository(session)


def get_id_card_service(
    repository: Annotated[IdCardInterface, Depends(get_id_card_repository)],
    session: DB_Session,
) -> IdCardService:
    return IdCardService(repository, session)


def get_subject_repository(
    session: DB_Session,
) -> SubjectInterface:
    return SubjectRepository(session)


def get_subject_service(
    repository: Annotated[SubjectInterface, Depends(get_subject_repository)],
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


def get_class_repository(session: DB_Session) -> ClassInterface:
    return ClassRepository(session)


def get_class_service(
    session: DB_Session,
    repository: Annotated[ClassInterface, Depends(get_class_repository)],
) -> ClassService:
    return ClassService(repository, session)
