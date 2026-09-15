from .exceptions import InvalidCalculationError
from .logger_config import setup_logger


logger = setup_logger()


def calculate():
    """Perform a basic calculation."""

    try:
        logger.debug("Calculation operation started")

        first_number = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            if second_number == 0:
                raise ZeroDivisionError(
                    "Cannot divide by zero"
                )

            result = first_number / second_number

        else:
            raise InvalidCalculationError(
                f"Unsupported operator: {operator}"
            )

        print("Result:", result)

        logger.info(
            "Calculation completed: %s %s %s = %s",
            first_number,
            operator,
            second_number,
            result
        )

    except ValueError:
        logger.error(
            "Non-numeric value entered during calculation"
        )
        print("Please enter valid numbers.")

    except ZeroDivisionError as error:
        logger.error("Calculation failed: %s", error)
        print(error)

    except InvalidCalculationError as error:
        logger.error("Invalid calculation: %s", error)
        print(error)

    except Exception:
        logger.exception(
            "Unexpected calculation failure"
        )
        print("Unexpected calculation error.")