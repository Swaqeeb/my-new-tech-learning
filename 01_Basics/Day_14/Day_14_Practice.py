# Python — Day 14 Practice
# Date: 07 Oct 2026
# Topic: Function Arguments, *args, **kwargs

# 1. Default parameter
def greet(name="Guest"):
    print("Hello", name)

greet("Swaqeeb")
greet()

# 2. Positional and keyword arguments
def employee_info(name, department, location):
    print(name, department, location)

employee_info("Rahim", "Finance", "Chattogram")
employee_info(location="Chattogram", name="Rahim", department="Finance")

# 3. Mixing positional, keyword, and default arguments
def employee_salary(name, salary, department="IT"):
    print(name, salary, department)

employee_salary("Swaqeeb", 50000)
employee_salary("Rahim", 60000, department="Finance")
employee_salary("Karim", 70000, department="HR")
employee_salary("Ayesha", 80000)
employee_salary("Nadia", 90000, department="HR")

# 4. *args — variable positional arguments
def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    print(total)

add_numbers(34, 56, 54)
add_numbers(34, 56, 54, 456, 54, 344)

# 5. **kwargs — variable keyword arguments
def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details(name="alok", course="Higher Math", city="Dhaka", age=34)

# 6. Final challenge
def employee_details(**details):
    for key, value in details.items():
        print(key, value)

employee_details(
    name="moonim",
    department="logic",
    location="Dhaka",
    salary=500000
)
