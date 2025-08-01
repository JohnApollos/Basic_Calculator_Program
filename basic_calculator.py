def basic_calculator():
    print("Welcome to the Basic Calculator Program!")

    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))

        # Get the second number from the user
        num2 = float(input("Enter the second number: "))

        # Get the mathematical operation from the user
        operation = input("Enter the operation (+, -, *, /): ")

        result = 0
        is_valid_operation = True

        # Perform the calculation based on the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:  # Prevent division by zero
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero!")
                is_valid_operation = False
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
            is_valid_operation = False

        # Display the result if the operation was valid
        if is_valid_operation and not (operation == '/' and num2 == 0):
            print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to run the calculator
basic_calculator()