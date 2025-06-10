import string

# Step 1: Input the Password
password = input("Enter a password: ")

# Step 2: Evaluate the Password
length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)

# Gather missing criteria
issues = []
if not length_ok:
    issues.append("at least 8 characters")
if not has_upper:
    issues.append("one uppercase letter")
if not has_lower:
    issues.append("one lowercase letter")
if not has_digit:
    issues.append("one digit")
if not has_special:
    issues.append("one special character (like @, #, $)")

# Output result
if not issues:
    print("Your password is strong!")
else:
    print("Your password needs " + ", ".join(issues) + ".")

# Bonus: Strength Meter (out of 10)
score = 0
if length_ok:
    score += 2
if has_upper:
    score += 2
if has_lower:
    score += 2
if has_digit:
    score += 2
if has_special:
    score += 2

print(f"Password Strength Score: {score}/10")
if score < 6:
    print("Try making your password stronger.")
elif score < 10:
    print("Decent password, but could be better.")
else:
    print("Excellent password!")
