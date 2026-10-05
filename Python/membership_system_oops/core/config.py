from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path
import os
from typing import Optional

load_dotenv()


@dataclass
class Config:

    app: Optional[str]
    data_folder: Path
    cwd: Path
    members_file: Path
    memberships_file: Path
    cities: list[str]

    @classmethod
    def get_env(cls):
        cwd = Path.cwd()
        if os.getenv("DATA_FOLDER") is None:
            raise ValueError("DATA_FOLDER not found in .env")

        data_folder = Path.cwd() / os.getenv("DATA_FOLDER")
        return cls(
            app=os.getenv("APP"),
            cwd=cwd,
            data_folder=data_folder,
            members_file=data_folder / os.getenv("MEMBERS_FILE"),
            memberships_file=data_folder / os.getenv("MEMBERSHIPS_FILE"),
            cities=os.getenv("CITIES").split(","),
        )


config = Config.get_env()
