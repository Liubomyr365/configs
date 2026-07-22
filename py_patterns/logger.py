import logging
from typing import ClassVar


class _ColorFormatter(logging.Formatter):
    RESET = "\033[0m"
    COLORS: ClassVar = {
        logging.DEBUG: "\033[37m",
        logging.INFO: "\033[32m",
        logging.WARNING: "\033[33m",
        logging.ERROR: "\033[31m",
        logging.CRITICAL: "\033[41m",
    }

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        color = self.COLORS.get(record.levelno, self.RESET)
        return f"{color}{message}{self.RESET}"


class Logger:
    FMT_MSG = "{asctime} |{levelname:<7}|{name}, {lineno} | {message}"
    FMT_STYLE = "{"
    FMT_DATE = "%H:%M:%S"

    @classmethod
    def get_logger(cls, name: str):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            streamhandler = logging.StreamHandler()
            streamhandler.setLevel(logging.INFO)
            formatter = _ColorFormatter(cls.FMT_MSG, cls.FMT_DATE, cls.FMT_STYLE)
            streamhandler.setFormatter(formatter)
            logger.addHandler(streamhandler)
        return logger
