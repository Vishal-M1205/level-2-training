import csv
from repositories.data_repository import DataRepository
from pathlib import Path


class CSVRepository(DataRepository):

    def read(self, filepath: Path) -> list[dict]:
        try:
            with open(filepath) as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            print(e)

    def write(self, filepath: Path, payload: dict) -> None:
        try:
            with open(filepath, "w") as file:
                writer = csv.DictWriter(file, fieldnames=payload[0].keys())
                writer.writerows(payload)

        except Exception as e:
            print(e)
