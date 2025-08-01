# Basic Python Calculator Program

This is a simple command-line calculator program written in Python. It allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

* **User-Friendly Input:** Prompts the user to enter two numbers and the desired mathematical operation.
* **Basic Operations:** Supports `+` (addition), `-` (subtraction), `*` (multiplication), and `/` (division).
* **Error Handling:**
    * Gracefully handles non-numeric input for numbers.
    * Prevents division by zero errors.
    * Notifies the user of invalid operation inputs.
* **Clear Output:** Displays the full equation and its result (e.g., `10.0 + 5.0 = 15.0`).

## How it Works

The program functions by:

1.  **Prompting for Input:** It first asks the user to input two numerical values. These inputs are converted to `float` (floating-point numbers) to allow for decimal calculations.
2.  **Requesting Operation:** Next, it asks the user to enter the desired mathematical operation symbol (`+, -, *, /`).
3.  **Conditional Calculation:**
    * It uses `if-elif-else` statements to check the entered operation.
    * Based on the operation, it performs the corresponding arithmetic.
    * **Division Safety:** A specific check is included for the division operation (`/`) to ensure that the second number (divisor) is not zero, preventing a `ZeroDivisionError`.
4.  **Displaying Results:** Once the calculation is complete (and no errors occurred), it prints the original numbers, the operation, and the calculated result in an easy-to-read format.
5.  **Error Handling (`try-except`):**
    * A `try-except` block is wrapped around the input and calculation logic.
    * If the user enters text instead of numbers (`ValueError`), an informative message is displayed.
    * If an unsupported operation symbol is entered, a specific error message is shown.
    * General exceptions are also caught to provide robust error feedback.

## Getting Started

### Prerequisites

You need Python installed on your system. This code is compatible with Python 3.x.

### Running the Program

1.  **Save the code:** Save the provided Python code into a file named `calculator.py` (or any other `.py` extension).
2.  **Open a terminal/command prompt:** Navigate to the directory where you saved the file.
3.  **Run the script:** Execute the script using the Python interpreter:

    ```bash
    basic_calculator.py
    ```

4.  **Follow the prompts:** The program will then guide you through entering the numbers and the operation.
