from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.dependencies import get_class_service
from app.schemas.student_class import TopFiveStudents
from app.services.class_service import ClassService

router = APIRouter(prefix="/class", tags=["Class Statistics"])


@router.get("/top-five", response_model=TopFiveStudents, status_code=status.HTTP_200_OK)
async def get_top_five_students(
    service: Annotated[ClassService, Depends(get_class_service)],
):
    return await service.get_top_five_students()
