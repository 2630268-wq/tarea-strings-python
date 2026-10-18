# Python strings assignment
# Student: Raúl Alejandro Hernández Quilantán
# Teacher: Carlos Antonio Tovar García
# Student ID: 2630268
# Group: I.M 1-2

# Executive summary
# A string is a sequence of characters represented by the str data type in Python.
# Strings are immutable, so methods that transform text return a new string.
# This file contains six programs about names, email addresses, palindromes, sentence statistics,
# password strength, and fixed-width product labels. Each problem includes inputs, outputs,
# validations, and normal, border, and error test cases.

# Problem 1: Full name formatter (name + initials)
# Description:
# Normalize a person's full name, remove extra spaces, display it in title case,
# and generate initials separated by periods.
# Inputs: full_name, a string containing at least two words.
# Outputs: Formatted name and initials.
# Validations: Reject empty input and names with fewer than two words.
# Test cases:
# 1) Normal: "  juan   carlos tovar " "Juan Carlos Tovar", "J.C.T."
# 2) Border: "ana lopez" "Ana Lopez", "A.L."
# 3) Error: "   "  Error: invalid input

def problem_1():
    full_name = input("Enter your full name: ").strip()
    name_parts = full_name.split()

    if not full_name:
        print("Error: invalid input")
        return
    if len(name_parts) < 2:
        print("Error: enter at least two words")
        return

    formatted_name = " ".join(name_parts).title()
    initials = "".join(part[0].upper() + "." for part in name_parts)

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")

# Problem 2: Simple email validator (structure + domain)
# Description:
# Check a basic email structure: exactly one '@', a non-empty local part,
# a domain containing a dot, and no whitespace.
# Inputs: email_text, a string.
# Outputs: Valid email: true/false and, when valid, the domain.
# Validations: Reject empty input, spaces, missing parts, or an incorrect '@' count.
# Test cases:
# 1) Normal: "student@example.com" -> valid; domain "example.com"
# 2) Border: "a@b.co" -> valid; domain "b.co"
# 3) Error: "studentexample.com" -> invalid

def problem_2():
    email_text = input("Enter an email address: ").strip()

    if not email_text:
        print("Error: invalid input")
        print("Valid email: false")
        return

    at_position = email_text.find("@")
    valid_email = (
        email_text.count("@") == 1
        and " " not in email_text
        and "\t" not in email_text
        and at_position > 0
        and at_position < len(email_text) - 1
    )

    if valid_email:
        domain_part = email_text[at_position + 1:]
        valid_email = "." in domain_part and not domain_part.startswith(".") and not domain_part.endswith(".")

    print(f"Valid email: {str(valid_email).lower()}")
    if valid_email:
        print(f"Domain: {domain_part}")

# Problem 3: Palindrome checker (ignoring spaces and case)
# Description:
# Determine whether a phrase reads the same forward and backward,
# ignoring spaces and letter case.
# Inputs: phrase, a string.
# Outputs: Is palindrome: true/false and the normalized phrase.
# Validations: Reject empty input and normalized phrases shorter than 3 characters.
# Test cases:
# 1) Normal: "Anita lava la tina" true
# 2) Border: "aba"  true
# 3) Error: " a "  Error: phrase is too short

def problem_3():
    phrase = input("Enter a phrase: ").strip()

    if not phrase:
        print("Error: invalid input")
        return

    normalized_phrase = phrase.lower().replace(" ", "")
    if len(normalized_phrase) < 3:
        print("Error: phrase is too short")
        return

    is_palindrome = normalized_phrase == normalized_phrase[::-1]
    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {str(is_palindrome).lower()}")

# Problem 4: Sentence word stats (lengths and first/last word)
# Description:
# Normalize outer and repeated spaces, split the sentence into words,
# and report word count, first and last words, and shortest/longest words.
# Inputs: sentence, a string.
# Outputs: Word count, first word, last word, shortest word, longest word.
# Validations: Reject empty input and input that produces no words.
# Test cases:
# 1) Normal: "Python makes coding fun" -> 4 words; shortest "fun"; longest "Python"
# 2) Border: "Hello" 1 word; first and last are "Hello"
# 3) Error: "   "  Error: invalid input

def problem_4():
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    words = sentence.split()
    if not words:
        print("Error: no valid words")
        return

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)

    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")

# Problem 5: Password strength classifier
# Description:
# Classify a password using its length and character categories.
# Strong requires at least 8 characters, uppercase, lowercase, a digit, and a symbol.
# Medium is any password of at least 8 characters that does not meet all strong rules.
# Weak is any password shorter than 8 characters.
# Inputs: password_input, a string.
# Outputs: Password strength: weak/medium/strong.
# Validations: Reject an empty password; check its length before classification.
# Test cases:
# 1) Normal: "Robo2026!" strong
# 2) Border: "Password" medium
# 3) Error: "" Error: invalid input

def problem_5():
    password_input = input("Enter a password to classify: ")

    if not password_input:
        print("Error: invalid input")
        return

    has_upper = any(character.isupper() for character in password_input)
    has_lower = any(character.islower() for character in password_input)
    has_digit = any(character.isdigit() for character in password_input)
    has_symbol = any(not character.isalnum() for character in password_input)

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")

# Problem 6: Product label formatter (fixed-width text)
# Description:
# Build a product label with a product name and positive price.
# The final label must contain exactly 30 characters: pad with spaces or truncate.
# Inputs: product_name, a string; price_value, a positive number.
# Outputs: Label containing exactly 30 characters, displayed between quotes.
# Validations: Reject an empty product name and a nonnumeric or nonpositive price.
# Test cases:
# 1) Normal: product "Notebook", price "25.50" 30-character label
# 2) Border: product "P", price "0.01" 30-character label
# 3) Error: product "Pen", price "-2" Error: price must be positive

def problem_6():
    product_name = input("Enter product name: ").strip()
    price_text = input("Enter positive price: ").strip()

    if not product_name:
        print("Error: invalid product name")
        return

    try:
        price_value = float(price_text)
    except ValueError:
        print("Error: price must be numeric")
        return

    if price_value <= 0:
        print("Error: price must be positive")
        return

    label_base = f"Product: {product_name} | Price: ${price_value:.2f}"
    label = label_base[:30].ljust(30)
    print(f'Label: "{label}"')
    print(f"Label length: {len(label)}")

# Main menu

def main():
    while True:
        print("\n=== Python String Operations ===")
        print("1. Full name formatter")
        print("2. Simple email validator")
        print("3. Palindrome checker")
        print("4. Sentence word statistics")
        print("5. Password strength classifier")
        print("6. Product label formatter")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            problem_1()
        elif choice == "2":
            problem_2()
        elif choice == "3":
            problem_3()
        elif choice == "4":
            problem_4()
        elif choice == "5":
            problem_5()
        elif choice == "6":
            problem_6()
        elif choice == "0":
            print("Program finished.")
            break
        else:
            print("Error: invalid menu option")

if __name__ == "__main__":
    main()

# Conclusions
# Strings are essential for receiving, transforming, validating, and displaying text.
# strip() removes outer whitespace, lower() normalizes case, and split() separates words.
# join() can combine words with consistent spacing, while slicing extracts selected portions.
# Normalizing text before comparisons reduces errors caused by extra spaces or letter case.
# Clear validation prevents empty or incorrectly formatted data from being processed.
# Since strings are immutable, methods such as lower() and replace() return new strings.
# The exercises demonstrate how string methods and slices solve common text-processing tasks.

# References
# 1. Python Software Foundation, "Built-in Types — Text Sequence Type: str."
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2. Python Software Foundation, "String Methods."
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3. Python Software Foundation, "Built-in Functions."
#    https://docs.python.org/3/library/functions.html
# 4. Python Software Foundation, "Errors and Exceptions."
#    https://docs.python.org/3/tutorial/errors.html
# 5. Python Software Foundation, "More on Defining Functions."
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
