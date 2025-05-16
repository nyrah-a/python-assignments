import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")

def calculator():
    print("Welcome to the Error-Free Calculator!")
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            try:
                if choice == '1':
                    result = num1 + num2
                    operation = "Addition"
                elif choice == '2':
                    result = num1 - num2
                    operation = "Subtraction"
                elif choice == '3':
                    result = num1 * num2
                    operation = "Multiplication"
                elif choice == '4':
                    if num2 == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = num1 / num2
                    operation = "Division"
            except ZeroDivisionError as e:
                print("Oops! Division by zero is not allowed.")
                logging.error(f"ZeroDivisionError occurred: {e}")
            else:
                print(f"{operation} result: {result}")
            finally:
                print("Operation complete.\n")
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

calculator()
