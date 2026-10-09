from fastapi import APIRouter, status
from app.schemas.exam_mark import (
    ExamMarkPatch,
    ExamMarkResponse,
    ExamMarkCreate,
    ExamMarkUpdate,
)
import app.services.exam_mark_service as exam_mark_service

router = APIRouter(prefix="/exam-marks", tags=["Exam Mark Management"])


@router.get("/", response_model=list[ExamMarkResponse])
async def get_all_exam_marks():
    return await exam_mark_service.get_all_exam_marks()


@router.get("/{exam_mark_id}", response_model=ExamMarkResponse)
async def get_exam_mark_by_id(exam_mark_id: int):
    return await exam_mark_service.get_exam_mark_by_id(exam_mark_id)


@router.post("/", response_model=ExamMarkResponse, status_code=status.HTTP_201_CREATED)
async def create_exam_mark(exam_mark: ExamMarkCreate):
    return await exam_mark_service.create_exam_mark(exam_mark)


@router.put("/{exam_mark_id}", response_model=ExamMarkResponse)
async def update_exam_mark(exam_mark_id: int, exam_mark: ExamMarkUpdate):
    return await exam_mark_service.update_exam_mark(exam_mark_id, exam_mark)


@router.delete("/{exam_mark_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exam_mark(exam_mark_id: int):
    await exam_mark_service.delete_exam_mark(exam_mark_id)


@router.patch("/{exam_mark_id}", response_model=ExamMarkResponse)
async def patch_exam_mark(exam_mark_id: int, exam_mark: ExamMarkPatch):
    return await exam_mark_service.patch_exam_mark(exam_mark_id, exam_mark)
