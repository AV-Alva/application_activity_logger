import os

from .logger_config import setup_logger


logger = setup_logger()


def read_file():
    """Read content from a text file."""

    try:
        filename = input("Enter file path to read: ").strip()

        logger.debug("Attempting to read file: %s", filename)

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        if not content:
            logger.warning("File was empty: %s", filename)
            print("The file is empty.")

        else:
            print("\nFile content:")
            print(content)

            logger.info(
                "File read successfully: %s",
                filename
            )

    except FileNotFoundError:
        logger.error(
            "File could not be opened because it does not exist: %s",
            filename
        )
        print("File not found.")

    except PermissionError:
        logger.error(
            "Permission denied while reading: %s",
            filename
        )
        print("Permission denied.")

    except Exception:
        logger.exception(
            "Unexpected error while reading file"
        )
        print("Unable to read the file.")


def write_file():
    """Write content to a text file."""

    try:
        filename = input("Enter file path to write: ").strip()
        content = input("Enter content: ")

        logger.debug("Attempting to write file: %s", filename)

        parent_folder = os.path.dirname(filename)

        if parent_folder:
            os.makedirs(parent_folder, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        logger.info(
            "File written successfully: %s",
            filename
        )

        print("File written successfully.")

    except PermissionError:
        logger.error(
            "Permission denied while writing: %s",
            filename
        )
        print("Permission denied.")

    except Exception:
        logger.exception(
            "Unexpected error while writing file"
        )
        print("Unable to write the file.")