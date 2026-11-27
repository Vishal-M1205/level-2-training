from typing import Annotated
from fastapi import Path

StudentID = Annotated[int, Path(gt=0, description="The ID of the student")]
