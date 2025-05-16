#Task 1 – Writing Functions

# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Example usage
greet_user("Alice")
result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is {result}.")

#Task 2 - Using Default Parameters

# Function to describe a pet
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Example usage
describe_pet("Buddy")               # Uses default "dog"
describe_pet("Whiskers", "cat")     # Overrides default

#Task 3 - Functions with Variable Arguments

# Function to make a sandwich with any number of ingredients
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")

# Example usage
make_sandwich("Lettuce", "Tomato", "Cheese")

#Task 4 - Understanding Recursion

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive function to calculate nth Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(f"Factorial of 5 is {factorial(5)}.")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")
