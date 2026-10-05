import csv
import logging
from repositories.data_repository import DataRepository
from pathlib import Path

logger = logging.getLogger(__name__)

class CSVRepository(DataRepository):

    def read(self, filepath: Path) -> list[dict]:
        try:
            with open(filepath) as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            logger.exception(e)

    def write(self, filepath: Path, payload: dict) -> None:
        try:
            with open(filepath, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=payload[0].keys())
                writer.writeheader()
                writer.writerows(payload)

        except Exception as e:
            logger.exception(e)
