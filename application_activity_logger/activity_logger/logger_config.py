import logging
import os


def setup_logger():
    """Configure application and error log files."""

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("ActivityLogger")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Stores DEBUG and above
    application_handler = logging.FileHandler(
        "logs/application.log"
    )
    application_handler.setLevel(logging.DEBUG)
    application_handler.setFormatter(formatter)

    # Stores ERROR and CRITICAL
    error_handler = logging.FileHandler(
        "logs/error.log"
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    logger.addHandler(application_handler)
    logger.addHandler(error_handler)

    return logger