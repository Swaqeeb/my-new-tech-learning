# Python — Day 3: September 12
# Topic: Conditional statements

# ============================================================
# Exercise 1: Check if someone is an adult
# ============================================================

age = 20

if age >= 18:
    print("Adult")

# Expected output:
# Adult


# ============================================================
# Exercise 2: Check if someone is not an adult
# ============================================================

age = 15

if age >= 18:
    print("Adult")
else:
    print("Not adult")

# Expected output:
# Not adult


# ============================================================
# Exercise 3: Check for exactly 20
# ============================================================

age = 20

if age == 20:
    print("Exactly 20")

# Expected output:
# Exactly 20


# ============================================================
# Exercise 4: Age classification
# ============================================================

age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Expected output:
# Teenager


# ============================================================
# Exercise 5: Age classification using user input
# ============================================================

age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Example:
# If the user enters 34:
# Adult


# ============================================================
# Exercise 6: Marks classification
# ============================================================

Marks = input("Enter your marks: ")
Marks = int(Marks)

if Marks >= 80:
    print("Excellent")
elif Marks >= 60:
    print("Good")
elif Marks >= 40:
    print("Pass")
else:
    print("Fail")

# Example:
# If the user enters 85:
# Excellent


# ============================================================
# Day 3 key lessons
# ============================================================
# 1. if checks a condition.
# 2. elif checks another condition.
# 3. else runs when previous conditions are False.
# 4. > means greater than.
# 5. < means less than.
# 6. >= means greater than or equal to.
# 7. <= means less than or equal to.
# 8. == checks equality.
# 9. != checks inequality.
# 10. = is used for assignment.
# 11. Python uses indentation for code blocks.
# 12. input() returns a string.
# 13. int() can convert user input into an integer.
# 14. Conditions are checked from top to bottom.
# 15. The first matching condition is executed.
# 16. else does not have a condition.
# 17. Do not type ... manually in the Python shell.
