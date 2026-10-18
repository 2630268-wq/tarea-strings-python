 # Handling numbers and booleans in Python
# Name: Raúl Alejandro Hernández Quilantán
# Student ID: 2630268
# Group: I.M 1-2
# Teacher: Carlos Antonio Tovar García

# Executive Summary:
# The int type stores whole numbers, while float stores numbers with decimals.
# Boolean values are True and False, and comparisons produce these values.
# Boolean expressions can be combined with and, or, and not to make decisions.
# Input validation helps prevent invalid values from being used in calculations.
# Checking ranges and avoiding division by zero make programs safer and more reliable.
# This program contains six exercises using numeric types, comparisons, and logic.
# Each exercise documents its inputs, outputs, validations, and three test cases.
# The program also demonstrates conversions, rounding, arithmetic, and conditional statements.

# Good Practices:
# Use int for whole-number quantities and float for decimal quantities.
# Store intermediate calculations in descriptive variables instead of repeating expressions.
# Validate input values before performing calculations, including checking for negative values.
# Use clear variable names and output messages to make the program easier to understand.
# Interpret each boolean according to its label: True means the stated condition is met.


# Problem 1: Temperature converter and range flag
# Description:
# Converts a temperature from Celsius to Fahrenheit and Kelvin.
# It also identifies whether the Celsius temperature is at least 30 degrees.
#
# Inputs:
# - temp_c: temperature in degrees Celsius (float).
#
# Outputs:
# - Fahrenheit, Kelvin, and High temperature (True or False).
#
# Validations:
# - The input must be convertible to float.
# - The temperature in Kelvin cannot be below 0.0.
#
# Test cases:
# 1) Normal: temp_c = 30.0 Fahrenheit = 86.00, Kelvin = 303.15, High temperature = True.
# 2) Border: temp_c = -273.15 Kelvin = 0.00, High temperature = False.
# 3) Error: temp_c = -300 Error: invalid input (below absolute zero).
def problem_1():
    try:
        temp_c = float(input("Enter temperature in Celsius: "))
        temp_k = temp_c + 273.15

        # Reject temperatures below absolute zero.
        if temp_k < 0.0:
            print("Error: invalid input")
            return

        # Convert Celsius to Fahrenheit and check the temperature range.
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = temp_c >= 30.0

        print(f"Fahrenheit: {temp_f:.2f}")
        print(f"Kelvin: {temp_k:.2f}")
        print(f"High temperature: {str(is_high_temperature).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 2: Work hours and overtime payment
# Description:
# Calculates regular pay for up to 40 hours and overtime pay at 150% of the hourly rate.
# It also reports whether the worker worked overtime.
#
# Inputs:
# - hours_worked: hours worked during the week (float).
# - hourly_rate: payment per hour (float).
#
# Outputs:
# - Regular pay, overtime pay, total pay, and Has overtime.
#
# Validations:
# - hours_worked must be greater than or equal to 0.
# - hourly_rate must be greater than 0.
# - Both inputs must be convertible to float.
#
# Test cases:
# 1) Normal: 45 hours at 20.0 regular pay = 800.00, overtime pay = 150.00, total = 950.00.
# 2) Border: 40 hours at 20.0 regular pay = 800.00, overtime pay = 0.00, Has overtime = False.
# 3) Error: hours_worked = -1 Error: invalid input.
def problem_2():
    try:
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))

        # Validate the values before calculating payment.
        if hours_worked < 0 or hourly_rate <= 0:
            print("Error: invalid input")
            return

        # Separate regular hours from overtime hours.
        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40.0

        print(f"Regular pay: {regular_pay:.2f}")
        print(f"Overtime pay: {overtime_pay:.2f}")
        print(f"Total pay: {total_pay:.2f}")
        print(f"Has overtime: {str(has_overtime).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 3: Discount eligibility with booleans
# Description:
# Determines whether a customer qualifies for a 10% discount.
# Eligibility is based on student status, senior status, or a purchase of at least 1000.
#
# Inputs:
# - purchase_total: purchase amount (float).
# - is_student_text: YES or NO.
# - is_senior_text: YES or NO.
#
# Outputs:
# - Discount eligible and Final total.
#
# Validations:
# - purchase_total must be greater than or equal to 0.
# - Student and senior answers must be YES or NO, ignoring letter case and outer spaces.
#
# Test cases:
# 1) Normal: purchase = 500, student = YES, senior = NO eligible = True, final = 450.00.
# 2) Border: purchase = 1000, student = NO, senior = NO eligible = True, final = 900.00.
# 3) Error: student answer = MAYBE Error: invalid input.
def problem_3():
    try:
        purchase_total = float(input("Enter purchase total: "))
        is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
        is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

        # Validate the purchase amount and the two yes/no answers.
        if purchase_total < 0:
            print("Error: invalid input")
            return
        if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
            print("Error: invalid input")
            return

        # Convert the text answers into boolean values.
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= 1000.0

        # Apply a 10% discount only when the customer is eligible.
        if discount_eligible:
            final_total = purchase_total * 0.90
        else:
            final_total = purchase_total

        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {final_total:.2f}")
    except ValueError:
        print("Error: invalid input")


# Problem 4: Basic statistics of three integers
# Description:
# Calculates the sum, average, maximum, and minimum of three integers.
# It also checks whether all three numbers are even.
#
# Inputs:
# - n1, n2, and n3: three integers.
#
# Outputs:
# - Sum, Average, Max, Min, and All even.
#
# Validations:
# - Each input must be convertible to int.
# - Negative integers are allowed.
#
# Test cases:
# 1) Normal: 2, 4, 6  sum = 12, average = 4.00, max = 6, min = 2, all even = True.
# 2) Border: 0, -2, 2 sum = 0, average = 0.00, all even = True.
# 3) Error: input "3.5" for an integer Error: invalid input.
def problem_4():
    try:
        n1 = int(input("Enter the first integer: "))
        n2 = int(input("Enter the second integer: "))
        n3 = int(input("Enter the third integer: "))

        # Calculate the requested statistics.
        sum_value = n1 + n2 + n3
        average_value = sum_value / 3
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)

        # The expression is True only when all three values are even.
        all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

        print(f"Sum: {sum_value}")
        print(f"Average: {average_value:.2f}")
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"All even: {str(all_even).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# Evaluates loan eligibility using monthly income, monthly debt, and credit score.
# Eligibility requires income of at least 8000, a debt ratio no higher than 0.4, and a score of at least 650.
#
# Inputs:
# - monthly_income: monthly income (float).
# - monthly_debt: monthly debt payments (float).
# - credit_score: credit score (int).
#
# Outputs:
# - Debt ratio and Eligible.
#
# Validations:
# - monthly_income must be greater than 0.
# - monthly_debt and credit_score must be greater than or equal to 0.
# - Inputs must have the required numeric types.
#
# Test cases:
# 1) Normal: income = 10000, debt = 2000, score = 700 ratio = 0.20, eligible = True.
# 2) Border: income = 8000, debt = 3200, score = 650 ratio = 0.40, eligible = True.
# 3) Error: income = 0 Error: invalid input (division by zero is avoided).
def problem_5():
    try:
        monthly_income = float(input("Enter monthly income: "))
        monthly_debt = float(input("Enter monthly debt payments: "))
        credit_score = int(input("Enter credit score: "))

        # Validate values before calculating the debt ratio.
        if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
            print("Error: invalid input")
            return

        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0
            and debt_ratio <= 0.4
            and credit_score >= 650
        )

        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {str(eligible).lower()}")
    except ValueError:
        print("Error: invalid input")


# Problem 6: Body Mass Index (BMI) and category flags
# Description:
# Calculates BMI using weight in kilograms and height in meters.
# It reports whether the BMI is underweight, normal, or overweight according to the specified ranges.
#
# Inputs:
# - weight_kg: weight in kilograms (float).
# - height_m: height in meters (float).
#
# Outputs:
# - BMI rounded to two decimal places, Underweight, Normal, and Overweight.
#
# Validations:
# - weight_kg and height_m must both be greater than 0.
# - Both inputs must be convertible to float.
#
# Test cases:
# 1) Normal: weight = 70, height = 1.75 BMI = 22.86, Normal = True.
# 2) Border: weight = 56.7, height = 1.70 BMI = 19.62, Normal = True.
# 3) Error: height = 0 Error: invalid input (division by zero is avoided).
def problem_6():
    try:
        weight_kg = float(input("Enter weight in kilograms: "))
        height_m = float(input("Enter height in meters: "))

        # Validate positive values before dividing.
        if weight_kg <= 0 or height_m <= 0:
            print("Error: invalid input")
            return

        bmi = weight_kg / (height_m * height_m)

        # Check which BMI range contains the calculated value.
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {round(bmi, 2):.2f}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")
    except ValueError:
        print("Error: invalid input")


# Main menu: lets the user choose one of the six problems.
def main():
    while True:
        print("\nNumbers and Booleans in Python")
        print("1. Temperature converter")
        print("2. Work hours and overtime")
        print("3. Discount eligibility")
        print("4. Statistics of three integers")
        print("5. Loan eligibility")
        print("6. Body Mass Index (BMI)")
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
# Integers and floating-point numbers work together to represent whole quantities and decimals.
# Comparisons produce boolean values that can control decisions with if statements.
# Validating input ranges prevents invalid calculations and helps avoid division by zero.
# The and, or, and not operators combine conditions to express more complete rules.
# These techniques can be used in payroll, discounts, loan evaluation, and other practical programs.
# Testing normal, border, and invalid inputs helps confirm that a program behaves as expected.

# References:
# 1. Python Software Foundation, "Built-in Types," Python Documentation.
#    https://docs.python.org/3/library/stdtypes.html
# 2. Python Software Foundation, "Numeric Types — int, float, complex," Python Documentation.
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 3. Python Software Foundation, "Boolean Type - bool," Python Documentation.
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 4. Python Software Foundation, "Built-in Functions," Python Documentation.
#    https://docs.python.org/3/library/functions.html
# 5. Python Software Foundation, "Errors and Exceptions," Python Tutorial.
#    https://docs.python.org/3/tutorial/errors.html
