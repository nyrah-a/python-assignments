#Task 1 - Understanding Python Exceptions

while True:
    try:
        number = float(input("Enter a number: "))
        result = 100 / number
        print(f"100 divided by {number} is {result}")
        break
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

#Task 2 - Types of Exceptions

# IndexError: Happens when trying to access a list index that doesn't exist
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("IndexError occurred! List index out of range.")

# KeyError: Happens when trying to access a key that isn't in the dictionary
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")

# TypeError: Happens when using incompatible types (like string + int)
try:
    result = "Age: " + 25
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

#Task 3 - Using try...except...else...finally

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Invalid input! Please enter numbers only.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")
