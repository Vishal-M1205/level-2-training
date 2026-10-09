from fastapi import APIRouter, status, Header, Response, Request, Query, UploadFile
from app.core.config import config
from app.schemas.result import ResultResponse
from app.schemas.student import (
    StudentPatch,
    StudentResponse,
    StudentCreate,
    StudentUpdate,
    StudentListResponse,
)
import app.services.student_service as student_service
import app.services.result_service as result_service
from typing import Optional

router = APIRouter(prefix="/students", tags=["Student Management"])
#! tags - groups the endpoints in the docs


#! As we are using dict_row now the value is validated with the Model and creates a object
#! If the validation passes then the object is deserialized to  a JSON data
# * That JSON is sent to the Client by FastAPI


@router.post("/idcards")
async def upload_student_id_card(file: UploadFile):
    await student_service.upload_student_id_card(file)
    return {"name": file.filename, "size": file.size}


@router.get("/", response_model=StudentListResponse, summary="Gets all the students")
async def get_all_students(
    request: Request,
    response: Response,
    age: Optional[int] = None,
    gender: Optional[str] = None,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=5, le=10),
    user_agent: Optional[str] = Header(default=None),
):
    """
    Return all the students data,
    Explicitly mention the columns in the sql query,
    Uses context manager to close the connection and the cursor automatically,
    404 - for resource not found error,
    500 - for internal server error
    """
    print(
        user_agent
    )  #! getting the value from the headers - name should be same underscore converted to "-" and it is
    #! case-insensitive

    print(request.headers)  #! All the header value from the client
    print(request.cookies)

    response.headers["API-Name"] = config.app_name
    response.headers["API-Version"] = config.app_version

    #! Sending a header response

    return await student_service.get_all_students(page, limit, age=age, gender=gender)


@router.get("/{student_id}", response_model=StudentResponse)
async def get_student_by_id(student_id: int):
    """GET student data using id (path parameter)"""

    return await student_service.get_student_by_id(student_id)


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
async def create_student(student: StudentCreate):
    """Creates a new Student Data"""
    return await student_service.create_student(student)


@router.put("/{student_id}", response_model=StudentResponse)
async def update_student(student_id: int, student: StudentUpdate):
    """Updates the exisitng Student data by Student ID"""
    return await student_service.update_student(student_id, student)


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int):
    """Deletes the Student data by Student ID , return no body"""
    await student_service.delete_student(student_id)


@router.patch("/{student_id}", response_model=StudentResponse)
async def patch_student(student_id: int, student: StudentPatch):
    """Modifies the data based on the field values"""
    return await student_service.patch_student(student_id, student)


@router.get("/{student_id}/results", response_model=ResultResponse)
async def get_student_exam_result_by_id(student_id: int):
    """Returns the exam result consist of marks, total and grade"""
    return await result_service.get_student_exam_result_by_id(student_id)
