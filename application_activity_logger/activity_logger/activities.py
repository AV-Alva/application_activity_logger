from .logger_config import setup_logger


logger = setup_logger()


def login():
    """Log the user into the application."""

    username = input("Enter username: ").strip()

    if not username:
        logger.warning("Login attempted with empty username")
        print("Username cannot be empty.")
        return False

    logger.info("User logged in: %s", username)
    print("Login successful.")

    return True


def logout():
    """Log the user out."""

    logger.info("User logged out")
    print("Logout successful.")