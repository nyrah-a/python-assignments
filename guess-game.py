import random

def play_guessing_game():
    print("🎲 Welcome to the Number Guessing Game! 🎲")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts+1}/{max_attempts} – Your guess: "))
        except ValueError:
            print("⚠️  Oops, that's not a valid number. Try again!")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("📉 Too low! Try again.")
        elif guess > number_to_guess:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempt{'s' if attempts>1 else ''}! 🎉")
            break
    else:
        # This block runs if the while loop completes without a break
        print(f"\n💥 Game over! Better luck next time. The number was {number_to_guess}. 💥")

if __name__ == "__main__":
    play_guessing_game()
