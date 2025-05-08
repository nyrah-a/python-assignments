age = int(input("How old are you? "))
if age >= 18:
    print("🎉 Congratulations! You are eligible to vote. Go make a difference!")
else:
    years_left = 18 - age
    year_word = "year" if years_left == 1 else "years"
    print(f"⏳ Oops! You’re not eligible yet. But hey, only {years_left} more {year_word} to go!")
