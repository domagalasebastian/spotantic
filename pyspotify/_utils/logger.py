import logging
from datetime import datetime
from typing import Optional
from typing import Union

from pydantic import DirectoryPath
from pydantic import NewPath
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

ROOT_LOGGER_NAME = "pyspotify"
FORMAT_STR = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"


class LoggingSettings(BaseSettings):
    """Runtime logging configuration.

    Reads configuration from environment variables (and an optional`.env` file)
    using the `pyspotify_logging_` prefix.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="pyspotify_logging_",
        extra="ignore",
    )

    enable: bool = False
    """Master switch for package logging; when ``False`` logging is disabled"""

    debug: bool = False
    """When ``True`` the logger level is set to DEBUG, otherwise INFO."""

    logs_dir: Optional[Union[DirectoryPath, NewPath]] = None
    """Optional directory where session log files are created."""


class ColorFormatter(logging.Formatter):
    """Console formatter that wraps log messages with ANSI color codes.

    Colors are chosen per log level to improve readability in terminals.
    """

    __RESET = "\033[0m"
    __LEVEL_COLORS = {
        logging.DEBUG: "\033[94m",
        logging.INFO: "\033[92m",
        logging.WARNING: "\033[93m",
        logging.ERROR: "\033[91m",
        logging.CRITICAL: "\033[1;91m",
    }

    def format(self, record: logging.LogRecord) -> str:
        """Format a LogRecord and wrap it in ANSI color sequences.

        Args:
            record: the LogRecord to format.

        Returns:
            The formatted log message string with ANSI color codes.
        """
        msg = super().format(record)
        color = self.__LEVEL_COLORS.get(record.levelno)

        return f"{color}{msg}{self.__RESET}"


def _setup_root_logger() -> logging.Logger:
    """Configure and return the package root logger.

    Behavior:
    - Loads `LoggingSettings` from environment/.env.
    - If `enable` is False, logging is disabled at the CRITICAL level and
        the root logger is returned unconfigured.
    - Otherwise the root logger `pyspotify` is configured with:
        - a console handler using `ColorFormatter` (INFO or DEBUG based on
            settings), and
        - when `logs_dir` is provided, a timestamped subdirectory is
            created and a `session.log` file handler is added.

    The function sets appropriate handler levels and the root logger's
    level according to `debug`.

    Returns:
        The configured package root :class:`logging.Logger` instance.
    """
    logging_settings = LoggingSettings()
    root_logger = logging.getLogger(ROOT_LOGGER_NAME)
    root_logger.propagate = False
    if not logging_settings.enable:
        root_logger.setLevel(logging.CRITICAL)
        return root_logger

    logging_level = logging.DEBUG if logging_settings.debug else logging.INFO
    root_logger.setLevel(logging_level)

    if logging_settings.logs_dir:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        logs_path = logging_settings.logs_dir / timestamp
        logs_path.mkdir(parents=True, exist_ok=True)

        session_filename = logs_path / "session.log"
        session_file_handler = logging.FileHandler(session_filename, mode="a", encoding="utf-8")
        session_file_handler.setLevel(logging_level)
        session_file_handler.setFormatter(logging.Formatter(FORMAT_STR))
        root_logger.addHandler(session_file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging_level)
    console_handler.setFormatter(ColorFormatter(FORMAT_STR))
    root_logger.addHandler(console_handler)

    return root_logger


logger = _setup_root_logger()
