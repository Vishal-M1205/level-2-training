import logging


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        filename="app.log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s ",
    )
