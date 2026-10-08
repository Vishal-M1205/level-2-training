from fastapi import APIRouter, status
from app.schemas.subject import (
    SubjectPatch,
    SubjectResponse,
    SubjectCreate,
    SubjectUpdate,
)
import app.services.subject_service as subject_service

router = APIRouter(prefix="/subjects")


@router.get("/", response_model=list[SubjectResponse])
async def get_all_subjects():
    """Return all the subjects data"""
    return await subject_service.get_all_subjects()


@router.get("/{subject_id}", response_model=SubjectResponse)
async def get_subject_by_id(subject_id: int):
    """GET subject data using id (path parameter)"""
    return await subject_service.get_subject_by_id(subject_id)


@router.post("/", response_model=SubjectResponse, status_code=status.HTTP_201_CREATED)
async def create_subject(subject: SubjectCreate):
    """Creates a new Subject Data"""
    return await subject_service.create_subject(subject)


@router.put("/{subject_id}", response_model=SubjectResponse)
async def update_subject(subject_id: int, subject: SubjectUpdate):
    """Updates the existing Subject data by Subject ID"""
    return await subject_service.update_subject(subject_id, subject)


@router.delete("/{subject_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subject(subject_id: int):
    """Deletes the Subject data by Subject ID, return no body"""
    await subject_service.delete_subject(subject_id)


@router.patch("/{subject_id}", response_model=SubjectResponse)
async def patch_subject(subject_id: int, subject: SubjectPatch):
    """Partially updates the Subject data by Subject ID"""
    return await subject_service.patch_subject(subject_id, subject)



