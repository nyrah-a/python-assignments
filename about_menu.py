import turtle

# Step 2: Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Step 3: Recursive Fibonacci Function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Step 4: Recursive Fractal Pattern (Bonus)
def draw_fractal_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Step 5: Menu and Input Handling
def main():
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        
        choice = input("> ").strip()

        if choice == "1":
            try:
                num = int(input("Enter a number to find its factorial: "))
                if num < 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The factorial of {num} is {factorial(num)}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        
        elif choice == "2":
            try:
                pos = int(input("Enter the position of the Fibonacci number: "))
                if pos < 0:
                    print("Please enter a non-negative integer.")
                else:
                    print(f"The {pos}th Fibonacci number is {fibonacci(pos)}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        
        elif choice == "3":
            print("Drawing a recursive fractal tree... (close the window to continue)")
            screen = turtle.Screen()
            screen.bgcolor("white")
            t = turtle.Turtle()
            t.color("green")
            t.left(90)
            t.speed(0)
            draw_fractal_tree(100, t)
            screen.exitonclick()

        elif choice == "4":
            print("Thank you for exploring recursion. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()
