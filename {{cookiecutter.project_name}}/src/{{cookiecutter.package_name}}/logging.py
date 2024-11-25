"""Logger initialization"""

import logging
from typing import Any, Optional


def config_logger(loglevel: int, log_file: Optional[str] = None) -> Any:
    """Initialize a custom logger"""
    logger = logging.getLogger()
    logger.setLevel(loglevel)
    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)
    console_handler.setFormatter(formatter)
    if log_file:
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        logger.addHandler(file_handler)
        file_handler.setFormatter(formatter)