import logging
from pathlib import Path

import aiofiles
from fastapi import HTTPException, UploadFile, status
from psycopg.errors import UniqueViolation

from app.repositories.id_card_repository import IdCardRepository
from app.schemas.id_card import IdCardCreate
from app.utils.path_utils import generate_file_path


class IdCardService:

    def __init__(self, repository: IdCardRepository):
        self.logger = logging.getLogger(__name__)
        self.repository = repository

    async def upload_student_id_card(self, student_id: int, file: UploadFile):
        try:
            if file.size > (1024 * 1024) * 10:
                raise HTTPException(status_code=status.HTTP_413_CONTENT_TOO_LARGE)

            supported_fileformat = [".png", ".jpg", ".jpeg"]

            if Path(file.filename).suffix not in supported_fileformat:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Unsupported file format, supported fileformats are {",".join(supported_fileformat)}",
                )

            id_card_file_path = generate_file_path(file, "uploads")

            stored_filename = Path(id_card_file_path).name

            file_content = await file.read()

            async with aiofiles.open(id_card_file_path, "wb") as id_card_file:
                await id_card_file.write(file_content)

            id_card_payload = IdCardCreate.model_validate(
                {
                    "student_id": student_id,
                    "original_filename": file.filename,
                    "stored_filename": stored_filename,
                    "file_path": str(id_card_file_path),
                }
            )

            id_card = await self.repository.upload_student_id_card(id_card_payload)

            if id_card is None:
                raise HTTPException(status_code=404, detail="ID Card Not Found")

            return id_card

        except UniqueViolation:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="ID Card Already Found"
            )

        except HTTPException:
            raise

        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=500, detail="Internal Server Error")
