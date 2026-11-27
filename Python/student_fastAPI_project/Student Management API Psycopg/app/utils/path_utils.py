from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile


def generate_file_path(file: bytes | UploadFile, dir: str):
    directory = Path(dir)

    Path.mkdir(directory, parents=True, exist_ok=True)

    extension = Path(file.filename).suffix

    return directory / f"{uuid4()}.{extension}"
