
# Countdown Timer

# Ask the user for a starting number
start = int(input("Enter the starting number: "))

# Use a while loop to count down from start to 1
current = start
while current > 0:
    print(current, end=' ')
    current -= 1

# When the loop finishes, print the celebratory message
print("Blast off!")

# Multiplication Table Generator

# Ask the user for a number
num = int(input("Enter a number: "))

# Use a for loop to print the table from 1 to 10
for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")
  
# Factorial Calculator

# Ask the user for a number
n = int(input("Enter a number: "))

# Use a for loop to compute the factorial
factorial = 1
for i in range(2, n + 1):
    factorial *= i

# Print the result
print(f"The factorial of {n} is {factorial}.")
