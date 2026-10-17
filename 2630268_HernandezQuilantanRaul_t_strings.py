content = r'''# =====================================================================
# ASSIGNMENT: STRING HANDLING IN PYTHON
# Student: Raúl Alejandro Hernández Quilantán
# Student ID: 2630268
# Group: I.M 1-2
# Subject: Manejo de strings en Python
# Teacher: M.C. Carlos Antonio Tovar García
# Due date: October 18, 2026
# File: 2630268_HernandezQuilantanRaul_t_strings.py
# =====================================================================

# EXECUTIVE SUMMARY
# A string is a sequence of characters used to store text.
# Strings are immutable, so string methods return a new string.
# This assignment processes names, email addresses, phrases, sentences,
# passwords, and product labels.
# The allowed string methods in this version are title(), upper(), lower(),
# lstrip(), rstrip(), join(), and strip().
# Other tasks are solved with loops, indexing, slicing, comparisons, and len().
# Each problem includes input checks and three example test cases.
#
# GOOD PRACTICES
# 1. Strings are immutable; transformations create a new string.
# 2. Remove unnecessary outer spaces before processing input.
# 3. Use clear variable names and readable validation messages.
# 4. Check empty input before processing it.
# 5. Use loops when a task cannot be solved with the allowed methods alone.
# 6. This version intentionally does not use split(), replace(), find(),
#    count(), startswith(), endswith(), isupper(), islower(), isdigit(),
#    isalnum(), or other string methods outside the allowed list.


# ============================================================
# Problem 1: Full name formatter (name + initials)
# Description:
# Clean a full name, format it in title case, and display initials.
# Inputs: full_name, a person's full name.
# Outputs: Formatted name and initials.
# Validations: Reject blank input and require at least two words.
# Test cases:
# 1) Normal: "  JUAN   carlos tovar " -> "Juan Carlos Tovar", "J.C.T."
# 2) Border: "Ana Ruiz" -> "Ana Ruiz", "A.R."
# 3) Error: "   " -> invalid input.
# ============================================================

def problem_1():
    full_name = input("Enter your full name: ")
    full_name = full_name.strip()

    if full_name == "":
        print("Error: name cannot be empty.")
        return

    # Convert tabs and repeated spaces into ordinary single spaces.
    cleaned_characters = []
    previous_was_space = False

    for character in full_name:
        if character == " " or character == "\t":
            if not previous_was_space:
                cleaned_characters.append(" ")
            previous_was_space = True
        else:
            cleaned_characters.append(character)
            previous_was_space = False

    cleaned_name = "".join(cleaned_characters).strip()
    words = []
    current_word = ""

    for character in cleaned_name:
        if character == " ":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += character

    if current_word != "":
        words.append(current_word)

    if len(words) < 2:
        print("Error: enter at least two words.")
        return

    formatted_name = cleaned_name.title()
    initials_parts = []

    for word in words:
        initials_parts.append(word[0].upper() + ".")

    initials = "".join(initials_parts)
    print("Formatted name:", formatted_name)
    print("Initials:", initials)


# ============================================================
# Problem 2: Simple email validator
# Description:
# Check a basic email structure and show its domain when valid.
# Inputs: email_text, an email address.
# Outputs: Valid email true/false and domain when valid.
# Validations: Reject blank input, spaces, missing parts, and incorrect @ count.
# Test cases:
# 1) Normal: "student@example.com" -> valid, domain "example.com".
# 2) Border: "a@b.co" -> valid, domain "b.co".
# 3) Error: "studentexample.com" -> invalid.
# ============================================================

def problem_2():
    email_text = input("Enter an email address: ").strip()

    if email_text == "":
        print("Error: invalid input.")
        print("Valid email: false")
        return

    at_count = 0
    at_position = -1
    has_space = False

    for index in range(len(email_text)):
        character = email_text[index]
        if character == "@":
            at_count += 1
            at_position = index
        if character == " " or character == "\t":
            has_space = True

    valid_email = at_count == 1 and not has_space
    valid_email = valid_email and at_position > 0
    valid_email = valid_email and at_position < len(email_text) - 1

    domain_part = ""
    if valid_email:
        domain_part = email_text[at_position + 1:]
        has_dot = False
        for character in domain_part:
            if character == ".":
                has_dot = True
        valid_email = has_dot and domain_part[0] != "."
        valid_email = valid_email and domain_part[-1] != "."

    print("Valid email:", str(valid_email).lower())
    if valid_email:
        print("Domain:", domain_part)


# ============================================================
# Problem 3: Palindrome checker
# Description:
# Check whether a phrase reads the same forward and backward,
# ignoring spaces and letter case.
# Inputs: phrase, a text phrase.
# Outputs: Normalized phrase and palindrome true/false.
# Validations: Reject blank input and normalized phrases shorter than 3 characters.
# Test cases:
# 1) Normal: "Anita lava la tina" -> true.
# 2) Border: "aba" -> true.
# 3) Error: " a " -> phrase is too short.
# ============================================================

def problem_3():
    phrase = input("Enter a phrase: ").strip()

    if phrase == "":
        print("Error: phrase cannot be empty.")
        return

    phrase = phrase.lower()
    normalized_characters = []

    for character in phrase:
        if character != " " and character != "\t":
            normalized_characters.append(character)

    normalized_phrase = "".join(normalized_characters)

    if len(normalized_phrase) < 3:
        print("Error: phrase is too short.")
        return

    reversed_phrase = ""
    for index in range(len(normalized_phrase) - 1, -1, -1):
        reversed_phrase += normalized_phrase[index]

    print("Normalized phrase:", normalized_phrase)
    print("Is palindrome:", str(normalized_phrase == reversed_phrase).lower())


# ============================================================
# Problem 4: Sentence word statistics
# Description:
# Count words and identify the first, last, shortest, and longest words.
# Inputs: sentence, a sentence.
# Outputs: Word count, first/last word, shortest/longest word.
# Validations: Reject blank input.
# Test cases:
# 1) Normal: "Python makes useful tools" -> 4 words; first Python; last tools.
# 2) Border: "Programming" -> 1 word.
# 3) Error: "   " -> invalid input.
# ============================================================

def problem_4():
    sentence = input("Enter a sentence: ").strip()

    if sentence == "":
        print("Error: sentence cannot be empty.")
        return

    words = []
    current_word = ""

    for character in sentence:
        if character == " " or character == "\t":
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += character

    if current_word != "":
        words.append(current_word)

    if len(words) == 0:
        print("Error: no words found.")
        return

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
        if len(word) > len(longest_word):
            longest_word = word

    print("Word count:", len(words))
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


# ============================================================
# Problem 5: Password strength classifier
# Description:
# Classify a password as weak, medium, or strong.
# Rules: weak if shorter than 8; strong if it has uppercase, lowercase,
# a digit, and a symbol; otherwise medium when length is at least 8.
# Inputs: password_input, a password.
# Outputs: Password strength.
# Validations: Reject blank input.
# Test cases:
# 1) Normal: "Abcdef1!" -> strong.
# 2) Border: "abcdefgh" -> medium.
# 3) Error: blank input -> invalid input.
# ============================================================

def problem_5():
    password_input = input("Enter a password: ").strip()

    if password_input == "":
        print("Error: password cannot be empty.")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_upper = True
        elif character in "abcdefghijklmnopqrstuvwxyz":
            has_lower = True
        elif character in "0123456789":
            has_digit = True
        else:
            has_symbol = True

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print("Password strength:", strength)


# ============================================================
# Problem 6: Product label formatter
# Description:
# Create a product label that is exactly 30 characters long.
# Inputs: product_name and price_text.
# Outputs: A fixed-width label.
# Validations: Reject blank product names and nonpositive/non-numeric prices.
# Test cases:
# 1) Normal: product "Notebook", price "25.50".
# 2) Border: product "P", price "0.01".
# 3) Error: product "Pen", price "-2" -> price must be positive.
# ============================================================

def problem_6():
    product_name = input("Enter product name: ").strip()
    price_text = input("Enter positive price: ").strip()

    if product_name == "":
        print("Error: product name cannot be empty.")
        return

    try:
        price_value = float(price_text)
    except ValueError:
        print("Error: price must be numeric.")
        return

    if price_value <= 0:
        print("Error: price must be positive.")
        return

    price_display = "{:.2f}".format(price_value)
    label_base = "Product: " + product_name + " | Price: $" + price_display

    if len(label_base) > 30:
        label = label_base[:30]
    else:
        label = label_base + (" " * (30 - len(label_base)))

    print('Label: "' + label + '"')
    print("Label length:", len(label))


# ============================================================
# MAIN MENU
# ============================================================

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
            print("Error: invalid menu option.")


if __name__ == "__main__":
    main()


# ============================================================
# CONCLUSIONS
# Strings are useful for receiving, transforming, validating, and displaying text.
# strip() removes spaces from the beginning and end of a string.
# title(), upper(), and lower() change letter case in a returned string.
# join() combines pieces of text, while loops can inspect characters one by one.
# Input validation helps prevent empty or incorrectly structured data.
# The six exercises show how basic loops, indexing, comparisons, and the allowed
# string methods can solve practical text-processing tasks.
#
# REFERENCES
# 1. Python Software Foundation, "Built-in Types: Text Sequence Type — str."
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2. Python Software Foundation, "Built-in Functions."
#    https://docs.python.org/3/library/functions.html
# 3. Python Software Foundation, "More Control Flow Tools."
#    https://docs.python.org/3/tutorial/controlflow.html
# 4. Python Software Foundation, "An Informal Introduction to Python."
#    https://docs.python.org/3/tutorial/introduction.html
# 5. Python Software Foundation, "Errors and Exceptions."
#    https://docs.python.org/3/tutorial/errors.html
#
# GITHUB REPOSITORY
# Add the URL of your GitHub repository here before submitting.
# ============================================================
'''
path = "/mnt/data/2630268_HernandezQuilantanRaul_t_strings.py"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Created: {path}")
