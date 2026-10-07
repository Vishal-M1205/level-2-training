from fastapi import APIRouter, status
from app.models.student import (
    StudentPatch,
    StudentResponse,
    StudentCreate,
    StudentUpdate,
)
import app.services.student_service as student_service

router = APIRouter(prefix="/students")


#! As we are using dict_row now the value is validated with the Model and creates a object
#! If the validation passes then the object is deserialized to  a JSON data
# * That JSON is sent to the Client by FastAPI


@router.get("/", response_model=list[StudentResponse])
def get_all_students():
    """
    Return all the students data,
    Explicitly mention the columns in the sql query,
    Uses context manager to close the connection and the cursor automatically,
    404 - for resource not found error,
    500 - for internal server error
    """
    return student_service.get_all_students()


@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int):
    """GET student data using id (path parameter)"""

    return student_service.get_student_by_id(student_id)


"""
Here the response model is for, after creating the data the API need to 
send back the newly created data.

 student: StudentCreate -> this is for the data sent from JSON body,
 the data is validated/serialized to a StudentCreate object

 By default API sends 200 for the below POST method.
 201 need to be used , for that 
 status_code=status.HTTP_201_CREATED 

 status imported from FastAPI 
"""


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    """Creates a new Student Data"""
    return student_service.create_student(student)


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate):
    """Updates the exisitng Student data by Student ID"""
    return student_service.update_student(student_id, student)


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    """Deletes the Student data by Student ID , return no body"""
    student_service.delete_student(student_id)


@router.patch("/{student_id}")
def patch_student(student_id: int, student: StudentPatch):
    return student_service.patch_student(student_id, student)
