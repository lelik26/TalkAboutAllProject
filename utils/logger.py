# utils/logger.py
import logging
from logging.handlers import RotatingFileHandler
from config import LOG_FORMAT, LOG_FILE

def setup_logger(name: str) -> logging.Logger:
    """Настраивает и возвращает логгер с ротацией файлов."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(LOG_FORMAT)

    # Консольный обработчик
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Файловый обработчик с ротацией
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=5)
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
