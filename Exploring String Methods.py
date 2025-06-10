# --- Task 1: String Slicing and Indexing ---
print("🔹 Task 1: String Slicing and Indexing")

text = "Python is amazing!"

first_word = text[:6]
amazing_part = text[10:17]
reversed_text = text[::-1]

print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_text)

# --- Task 2: String Methods ---
print("\n🔹 Task 2: String Methods")

msg = " hello, python world! "

stripped = msg.strip()
capitalized = stripped.capitalize()
replaced = stripped.replace("world", "universe")
uppercased = stripped.upper()

print("Stripped string:", stripped)
print("Capitalized string:", capitalized)
print("Replaced string:", replaced)
print("Uppercased string:", uppercased)

# --- Task 3: Palindrome Checker ---
print("\n🔹 Task 3: Palindrome Checker")

word = input("Enter a word: ").strip()
reversed_word = word[::-1]

if word.lower() == reversed_word.lower():
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is not a palindrome. Try another one!")
