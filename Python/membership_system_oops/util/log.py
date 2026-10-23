import logging


def setup_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.FileHandler(filename="app.log")],
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s ",
    )
