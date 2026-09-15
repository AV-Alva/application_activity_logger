# Application Activity Logger

## 📌 Project Overview

The **Application Activity Logger** is a menu-driven Python application created to demonstrate the practical use of Python's **logging** and **exception handling** features.

The application allows a user to perform different activities such as:

1. Login
2. Perform calculations
3. Read a file
4. Write to a file
5. Logout
6. Exit the application

The main objective of this project is to understand how real-world applications record different events using Python's `logging` module.

The application generates logs at different severity levels:

* `DEBUG`
* `INFO`
* `WARNING`
* `ERROR`
* `CRITICAL`

Exception handling is used throughout the application so that an error in one operation does not unnecessarily terminate the entire program.

---

# 🎯 Objectives

The objectives of this project are to:

* Understand Python's `logging` module
* Understand different logging levels
* Configure multiple log files
* Use logging across multiple Python modules
* Handle runtime errors using `try` and `except`
* Create custom exceptions
* Build a menu-driven Python application
* Understand Python packages and modules
* Separate application responsibilities into reusable modules
* Prevent individual operation failures from crashing the entire application

---

# 📂 Project Structure

```text
application_activity_logger/
│
├── activity_logger/
│   ├── __init__.py
│   ├── activities.py
│   ├── calculator.py
│   ├── file_operations.py
│   ├── exceptions.py
│   └── logger_config.py
│
├── logs/
│   ├── application.log
│   └── error.log
│
├── files/
│   └── sample.txt
│
├── main.py
└── README.md
```

---

# 📄 File Description

## `main.py`

This is the entry point of the application.

It:

* Displays the menu
* Accepts the user's choice
* Calls the appropriate functions
* Keeps the application running using a `while` loop
* Handles unexpected application-level exceptions
* Logs menu selections and application activities

The program continues running until the user explicitly selects **Exit**.

---

## `activity_logger/__init__.py`

This file identifies the `activity_logger` directory as a Python package.

It allows modules from the package to be imported into `main.py`.

Example:

```python
from activity_logger.calculator import calculate
```

---

## `activity_logger/logger_config.py`

This module contains the logging configuration for the application.

It creates the `logs` directory automatically if it does not already exist.

Two log files are maintained:

### `application.log`

Stores all application activities starting from the `DEBUG` level.

This can include:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

### `error.log`

Stores only serious application problems starting from the `ERROR` level.

This includes:

```text
ERROR
CRITICAL
```

Each log entry contains:

* Date
* Time
* Logging level
* Log message

Example:

```text
2026-09-15 20:10:01 - INFO - Application started
```

---

## `activity_logger/activities.py`

This module contains functions related to user activities.

The main operations are:

```text
Login
Logout
```

A successful login generates an `INFO` log.

Example:

```text
INFO - User logged in
```

An empty username can generate a `WARNING`.

Example:

```text
WARNING - Login attempted with empty username
```

---

## `activity_logger/calculator.py`

This module contains the calculator functionality.

Supported operations include:

```text
Addition
Subtraction
Multiplication
Division
```

The calculator handles errors such as:

* Non-numeric input
* Division by zero
* Unsupported mathematical operators
* Unexpected calculation errors

Example successful log:

```text
INFO - Calculation completed: 10 + 20 = 30
```

Example error:

```text
ERROR - Calculation failed: Cannot divide by zero
```

---

## `activity_logger/file_operations.py`

This module contains functions for:

* Reading files
* Writing files

The program handles file-related problems such as:

* File not found
* Empty files
* Permission errors
* Unexpected file operation errors

For example, reading an empty file generates:

```text
WARNING - File was empty
```

Trying to read a file that does not exist generates:

```text
ERROR - File could not be opened
```

---

## `activity_logger/exceptions.py`

This module contains custom exceptions used by the application.

For example:

```python
class InvalidCalculationError(Exception):
    """Raised when an invalid calculation is attempted."""
    pass
```

Custom exceptions make errors easier to understand and allow the application to handle specific problems more clearly.

---

# 📝 Understanding Logging Levels

Python provides different logging levels based on the seriousness of an event.

| Level    | Purpose                                                  | Example                        |
| -------- | -------------------------------------------------------- | ------------------------------ |
| DEBUG    | Detailed information useful during development           | User selected menu option      |
| INFO     | Normal successful application activity                   | User logged in                 |
| WARNING  | Something unusual happened, but the program can continue | File was empty                 |
| ERROR    | An operation failed                                      | File could not be opened       |
| CRITICAL | A serious unexpected application failure occurred        | Unexpected application failure |

The severity increases in the following order:

```text
DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL
```

---

# ⚠️ Exception Handling

Exception handling is an important part of this application.

Operations are placed inside `try` blocks.

Possible errors are handled using `except`.

Example:

```python
try:
    number = float(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number.")
```

Instead of allowing the entire application to terminate when an error occurs, the error is:

1. Caught
2. Logged
3. Displayed to the user
4. Handled appropriately
5. The application can continue

---

# 🔄 Application Flow

The basic application flow is:

```text
Start Application
       |
       v
Display Menu
       |
       v
User Selects Option
       |
       v
Perform Activity
       |
       v
Generate Log
       |
       v
Handle Errors if Any
       |
       v
Return to Menu
       |
       v
Exit Selected?
   /       \
 No         Yes
 |           |
Menu        Stop
```

The `while` loop keeps the menu running until the user selects **Exit**.

---

# ▶️ How to Run the Project

## Step 1: Clone the repository

```bash
git clone <your-github-repository-url>
```

## Step 2: Navigate to the project

```bash
cd application_activity_logger
```

## Step 3: Run the program

```bash
python main.py
```

The program should display:

```text
===== APPLICATION ACTIVITY LOGGER =====
1. Login
2. Calculate
3. Read a File
4. Write a File
5. Logout
6. Exit

Enter your choice:
```

---

# 🧪 Testing the Logging Levels

The application can be tested for each logging level.

### DEBUG

Select a menu option or start a calculation.

Example:

```text
DEBUG - User selected menu option: 2
```

### INFO

Perform a successful operation such as login.

Example:

```text
INFO - User logged in
```

### WARNING

Try reading an empty file.

Example:

```text
WARNING - File was empty
```

### ERROR

Try reading a file that does not exist.

Example:

```text
ERROR - File could not be opened because it does not exist
```

### CRITICAL

A `CRITICAL` log is reserved for serious and unexpected application-level failures.

Example:

```text
CRITICAL - Unexpected application failure
```

---

# 📊 Example `application.log`

```text
2026-09-15 20:10:01 - INFO - Application started
2026-09-15 20:10:05 - DEBUG - User selected menu option: 1
2026-09-15 20:10:10 - INFO - User logged in: Amruta
2026-09-15 20:10:15 - DEBUG - User selected menu option: 2
2026-09-15 20:10:20 - DEBUG - Calculation operation started
2026-09-15 20:10:25 - INFO - Calculation completed: 10.0 + 20.0 = 30.0
2026-09-15 20:10:35 - WARNING - File was empty
2026-09-15 20:10:45 - ERROR - File could not be opened because it does not exist
2026-09-15 20:11:00 - INFO - Application closed normally
```

---

# 📕 Example `error.log`

The `error.log` file contains only `ERROR` and `CRITICAL` messages.

```text
2026-09-15 20:10:45 - ERROR - File could not be opened because it does not exist
2026-09-15 20:12:15 - CRITICAL - Unexpected application failure
```

---

# 💡 Key Concepts Learned

Through this project, the following Python concepts are demonstrated:

* Python Logging
* DEBUG logging
* INFO logging
* WARNING logging
* ERROR logging
* CRITICAL logging
* Exception handling
* `try`
* `except`
* Custom exceptions
* File handling
* `with open()`
* Functions
* Modules
* Packages
* Imports
* `while` loops
* Conditional statements
* Menu-driven applications
* Separation of responsibilities

---

# 🛠 Technologies Used

* Python 3
* Python `logging` module
* Python `os` module
* File Handling
* Exception Handling
* Visual Studio Code

No external Python packages are required for this project.

---

# 🎓 Learning Outcome

This project demonstrates how logging can be used to understand what is happening inside an application.

Instead of relying only on `print()` statements, logs create a permanent record of:

* Successful operations
* User activities
* Warnings
* Errors
* Unexpected failures

This is especially useful in real-world applications because developers may not be present when an error occurs. Log files help developers investigate what happened and identify the cause of a problem.

The project also demonstrates how exception handling can make an application more fault tolerant by preventing individual errors from unnecessarily terminating the entire program.



**Keep Learning. Keep Building. Keep Evolving.**
