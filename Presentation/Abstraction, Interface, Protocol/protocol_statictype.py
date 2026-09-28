from typing import Protocol


class Storage(Protocol):
    def save(self, filename: str) -> None: ...


class LocalStorage:
    def save(self, filename: str) -> None:
        print(f"Saving {filename} locally")


class Printer:
    def print_document(self, filename: str) -> None:
        print(f"Printing {filename}")


def upload_file(storage: Storage):
    storage.save("report.pdf")


local = LocalStorage()
printer = Printer()

upload_file(local)


# pip install pyright
