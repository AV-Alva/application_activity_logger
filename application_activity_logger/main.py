from activity_logger.activities import login, logout
from activity_logger.calculator import calculate
from activity_logger.file_operations import read_file, write_file
from activity_logger.logger_config import setup_logger


logger = setup_logger()


def display_menu():
    """Display the application menu."""

    print("\n===== APPLICATION ACTIVITY LOGGER =====")
    print("1. Login")
    print("2. Calculate")
    print("3. Read a File")
    print("4. Write a File")
    print("5. Logout")
    print("6. Exit")


def main():
    """Run the application."""

    logger.info("Application started")

    while True:

        try:
            display_menu()

            choice = input("Enter your choice: ").strip()

            logger.debug("User selected menu option: %s", choice)

            if choice == "1":
                login()

            elif choice == "2":
                calculate()

            elif choice == "3":
                read_file()

            elif choice == "4":
                write_file()

            elif choice == "5":
                logout()

            elif choice == "6":
                logger.info("Application closed normally")
                print("Application closed.")
                break

            else:
                logger.warning(
                    "Invalid menu option entered: %s",
                    choice
                )
                print("Invalid choice. Please select 1-6.")

        except KeyboardInterrupt:
            logger.warning("Application interrupted by user")
            print("\nApplication interrupted.")
            break

        except Exception:
            logger.critical(
                "Unexpected application failure",
                exc_info=True
            )

            print(
                "An unexpected error occurred, "
                "but the application will continue."
            )


if __name__ == "__main__":
    main()