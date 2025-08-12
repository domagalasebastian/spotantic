import logging
import os
from datetime import datetime
from pathlib import Path

LOGS_DIR_NAME = "logs"
ROOT_LOGGER_NAME = "pyspotify"
FORMAT_STR = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"


logging.basicConfig(
    format=FORMAT_STR,
    level=logging.INFO,
)


class ColorFormatter(logging.Formatter):
    __RESET = "\033[0m"
    __LEVEL_COLORS = {
        logging.DEBUG: "\033[94m",
        logging.INFO: "\033[92m",
        logging.WARNING: "\033[93m",
        logging.ERROR: "\033[91m",
        logging.CRITICAL: "\033[1;91m",
    }

    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        color = self.__LEVEL_COLORS.get(record.levelno)

        return f"{color}{msg}{self.__RESET}"


def setup_root_logger() -> logging.Logger:
    root_logger = logging.getLogger(ROOT_LOGGER_NAME)
    root_logger.setLevel(logging.DEBUG)
    root_logger.propagate = False

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    logs_path = Path(os.getcwd()) / LOGS_DIR_NAME / timestamp
    logs_path.mkdir(parents=True, exist_ok=True)
    session_filename = logs_path / "session.log"
    debug_filename = logs_path / "debug.log"

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(ColorFormatter(FORMAT_STR))
    root_logger.addHandler(console_handler)

    session_file_handler = logging.FileHandler(session_filename, mode="a", encoding="utf-8")
    session_file_handler.setLevel(logging.INFO)
    session_file_handler.setFormatter(logging.Formatter(FORMAT_STR))
    root_logger.addHandler(session_file_handler)

    debug_file_handler = logging.FileHandler(debug_filename, mode="a", encoding="utf-8")
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(logging.Formatter(FORMAT_STR))
    root_logger.addHandler(debug_file_handler)

    return root_logger


logger = setup_root_logger()
