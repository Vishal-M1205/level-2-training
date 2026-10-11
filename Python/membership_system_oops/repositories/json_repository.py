import json
import logging
from repositories.data_repository import DataRepository
from pathlib import Path

logger = logging.getLogger(__name__)

class JsonRepository(DataRepository):

    def read(self, filepath: Path) -> list[dict]:
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError as e:
            logger.exception(f"{filepath} : not found")
        except json.JSONDecodeError as e:
            logger.exception(f"{filepath} : wrong JSON Format")

    def write(self, filepath: Path, payload: dict) -> None:
        try:
            data = payload
            with open(filepath, "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as e:
            logger.exception(f"{filepath} : not found")
        except json.JSONDecodeError as e:
            logger.exception(f"{filepath} : wrong JSON Format")
        else:
            print(f"{filepath} updated successfully")
