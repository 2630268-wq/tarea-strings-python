# Working with Lists, Tuples, and Dictionaries in Python
# Name: Raúl Alejandro Hernández Quilantán
# Student ID: 2630268
# Group: I.M 1-2
# Teacher: Carlos Antonio Tovar García

# Executive Summary:
# A list is an ordered, mutable collection that can store multiple elements.
# A tuple is an ordered, immutable collection used for data that should not change.
# A dictionary stores key-value pairs and allows information to be found by key.
# Lists can be modified, while tuples cannot be changed after creation.
# Dictionaries can be updated by adding, changing, or removing key-value pairs.
# This program contains six problems using lists, tuples, and dictionaries.
# Each problem documents its description, inputs, outputs, validations, and test cases.
# The program also demonstrates searching, sorting, calculations, and data management.

# Good Practices:
# Use lists when elements need to be added or removed.
# Use tuples for fixed data such as coordinates.
# Use dictionaries to find information through descriptive keys.
# Avoid changing a list while iterating over it unless necessary.
# Use clear variable names and messages that explain the result.
# Validate input before performing calculations or accessing stored data.


# Problem 1: Shopping list basics
# Description:
# Creates a list of products, adds a new product, and searches for an item.
# The program displays the list, its length, and whether the searched item exists.
#
# Inputs:
# - initial_items_text: comma-separated product names.
# - new_item: product name to add.
# - search_item: product name to search for.
#
# Outputs:
# - Items list, Total items, and Found item.
#
# Validations:
# - The initial list must not be empty.
# - Empty product names are removed from the initial list.
# - New and searched product names must not be empty.
#
# Test cases:
# 1) Normal: apple,banana; add orange; search bananaFound item: true.
# 2) Border: apple; add banana; search grape Found item: false.
# 3) Error: an empty initial list Error: invalid input.
def problem_1():
    initial_items_text = input("Enter products separated by commas: ").strip()

    if not initial_items_text:
        print("Error: invalid input")
        return

    # Split the input and remove extra spaces around each product.
    items_list = [
        item.strip()
        for item in initial_items_text.split(",")
        if item.strip()
    ]

    if not items_list:
        print("Error: invalid input")
        return

    new_item = input("Enter a product to add: ").strip()
    search_item = input("Enter a product to search for: ").strip()

    if not new_item or not search_item:
        print("Error: invalid input")
        return

    # Add the new product and check whether the requested product exists.
    items_list.append(new_item)
    is_in_list = search_item in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {len(items_list)}")
    print(f"Found item: {str(is_in_list).lower()}")


# Problem 2: Points and distances with tuples
# Description:
# Stores two points as tuples and calculates the Euclidean distance.
# It also calculates the midpoint between the two points.
#
# Inputs:
# - x1, y1, x2, y2: numeric coordinates.
#
# Outputs:
# - Point A, Point B, Distance, and Midpoint.
#
# Validations:
# - All four coordinates must be convertible to float.
# - Negative and decimal coordinates are allowed.
#
# Test cases:
# 1) Normal: A = (0, 0), B = (3, 4) Distance: 5.00, Midpoint: (1.5, 2.0).
# 2) Border: A = (2, 2), B = (2, 2) Distance: 0.00.
# 3) Error: enter "abc" for a coordinate Error: invalid input.
def problem_2():
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
    except ValueError:
        print("Error: invalid input")
        return

    # Tuples store the coordinates of each point.
    point_a = (x1, y1)
    point_b = (x2, y2)

    # Calculate the distance and the midpoint.
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance:.2f}")
    print(f"Midpoint: {midpoint}")


# Problem 3: Product catalog with dictionary
# Description:
# Stores product names and unit prices in a dictionary.
# It calculates the total cost when the requested product exists.
#
# Inputs:
# - product_name: product name.
# - quantity: number of units to purchase.
#
# Outputs:
# - Unit price, Quantity, and Total, or an error message.
#
# Validations:
# - The product name must not be empty.
# - Quantity must be a positive integer.
# - The requested product must exist in the dictionary.
#
# Test cases:
# 1) Normal: apple, quantity 3 Unit price: 10.00, Total: 30.00.
# 2) Border: banana, quantity 1 Total: 15.00.
# 3) Error: quantity 0 or an unknown product Error message.
def problem_3():
    # Each dictionary key identifies a product and its unit price.
    product_prices = {
        "apple": 10.0,
        "banana": 15.0,
        "orange": 12.5,
        "bread": 28.0
    }

    product_name = input("Enter product name: ").strip().lower()

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Error: invalid input")
        return

    if not product_name or quantity <= 0:
        print("Error: invalid input")
        return

    # Check the dictionary before accessing the product price.
    if product_name not in product_prices:
        print("Error: product not found")
        return

    unit_price = product_prices[product_name]
    total_price = unit_price * quantity

    print(f"Unit price: {unit_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price:.2f}")


# Problem 4: Student grades with dictionary and list
# Description:
# Stores student names and their grades in a dictionary of lists.
# It calculates the selected student's average and determines whether the student passed.
#
# Inputs:
# - student_name: name of the student.
#
# Outputs:
# - Grades, Average, and Passed, or an error message.
#
# Validations:
# - The student name must not be empty.
# - The student must exist in the dictionary.
# - The grade list must not be empty before calculating the average.
#
# Test cases:
# 1) Normal: Alice grades [90, 80, 85], average 85.00, Passed: true.
# 2) Border: Bob grades [70, 70, 70], average 70.00, Passed: true.
# 3) Error: unknown student name Error: student not found.
def problem_4():
    # Each student is associated with a list of grades.
    grades = {
        "alice": [90.0, 80.0, 85.0],
        "bob": [70.0, 70.0, 70.0],
        "charlie": [60.0, 65.0, 55.0]
    }

    student_name = input("Enter student name: ").strip().lower()

    if not student_name:
        print("Error: invalid input")
        return

    # Check that the student exists before retrieving the grades.
    if student_name not in grades:
        print("Error: student not found")
        return

    student_grades = grades.get(student_name, [])

    if not student_grades:
        print("Error: no grades available")
        return

    average = sum(student_grades) / len(student_grades)
    is_passed = average >= 70.0

    print(f"Grades: {student_grades}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {str(is_passed).lower()}")


# Problem 5: Word frequency counter
# Description:
# Converts a sentence into a list of lowercase words.
# It builds a dictionary containing each word and its frequency.
#
# Inputs:
# - sentence: a sentence entered by the user.
#
# Outputs:
# - Words list, Frequencies, and Most common word.
#
# Validations:
# - The sentence must not be empty.
# - Simple punctuation is removed before counting words.
# - The resulting list must contain at least one word.
#
# Test cases:
# 1) Normal: "cat dog cat" cat: 2, dog: 1, most common: cat.
# 2) Border: "hello" hello: 1, most common: hello.
# 3) Error: an empty sentence or punctuation only Error: invalid input.
def problem_5():
    import string

    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: invalid input")
        return

    # Replace punctuation with spaces and convert the sentence to lowercase.
    cleaned_sentence = sentence.translate(
        str.maketrans(string.punctuation, " " * len(string.punctuation))
    ).lower()

    words_list = cleaned_sentence.split()

    if not words_list:
        print("Error: invalid input")
        return

    freq_dict = {}

    # Count how many times each word appears.
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    # Find the word with the highest frequency.
    most_common_word = max(freq_dict, key=freq_dict.get)

    print(f"Words list: {words_list}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common_word}")


# Problem 6: Simple contact book
# Description:
# Uses a dictionary to store contact names and phone numbers.
# The user can add, search for, or delete a contact.
#
# Inputs:
# - action_text: ADD, SEARCH, or DELETE.
# - name: contact name.
# - phone: phone number, required for ADD.
#
# Outputs:
# - A message confirming the operation or reporting an error.
#
# Validations:
# - The action must be ADD, SEARCH, or DELETE.
# - The contact name must not be empty.
# - For ADD, the phone number must not be empty.
# - SEARCH and DELETE check that the contact exists.
#
# Test cases:
# 1) Normal: ADD, name David, phone 5551234567 Contact saved.
# 2) Border: SEARCH for an existing contact Phone is displayed.
# 3) Error: DELETE an unknown contact Error: contact not found.
def problem_6():
    # Contact names are dictionary keys and phone numbers are values.
    contacts = {
        "alice": "5551234567",
        "bob": "5559876543",
        "charlie": "5552468101"
    }

    action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

    if action_text not in ("ADD", "SEARCH", "DELETE"):
        print("Error: invalid input")
        return

    name = input("Enter contact name: ").strip()

    if not name:
        print("Error: invalid input")
        return

    # Normalize names to make searches consistent.
    name = name.lower()

    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()

        if not phone:
            print("Error: invalid input")
            return

        # Save a new contact or update an existing one.
        contacts[name] = phone
        print(f"Contact saved: {name}, {phone}")

    elif action_text == "SEARCH":
        # get() returns None when the contact does not exist.
        phone = contacts.get(name)

        if phone is None:
            print("Error: contact not found")
        else:
            print(f"Phone: {phone}")

    elif action_text == "DELETE":
        # pop() removes the contact only if the key exists.
        if name in contacts:
            contacts.pop(name)
            print(f"Contact deleted: {name}")
        else:
            print("Error: contact not found")


# Main menu: allows the user to select one of the six problems.
def main():
    while True:
        print("\nLists, Tuples, and Dictionaries in Python")
        print("1. Shopping list")
        print("2. Points and distances")
        print("3. Product catalog")
        print("4. Student grades")
        print("5. Word frequency")
        print("6. Contact book")
        print("0. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            problem_1()
        elif option == "2":
            problem_2()
        elif option == "3":
            problem_3()
        elif option == "4":
            problem_4()
        elif option == "5":
            problem_5()
        elif option == "6":
            problem_6()
        elif option == "0":
            print("Program finished.")
            break
        else:
            print("Error: invalid input")


# Conclusions:
# Lists are useful when a collection needs to be modified frequently.
# Tuples represent ordered data that should remain unchanged after creation.
# Dictionaries make it easier to retrieve and update information using keys.
# Combining dictionaries and lists is useful for organizing records such as grades.
# Searching and validating data prevents errors when a requested item is missing.
# Testing normal, border, and invalid inputs helps verify program behavior.

# References:
# 1. Python Software Foundation, "Data Structures," Python Tutorial.
#    https://docs.python.org/3/tutorial/datastructures.html
# 2. Python Software Foundation, "Built-in Types," Python Documentation.
#    https://docs.python.org/3/library/stdtypes.html
# 3. Python Software Foundation, "More on Lists," Python Tutorial.
#    https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# 4. Python Software Foundation, "Dictionaries," Python Tutorial.
#    https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# 5. Python Software Foundation, "Built-in Functions," Python Documentation.
#    https://docs.python.org/3/library/functions.html
