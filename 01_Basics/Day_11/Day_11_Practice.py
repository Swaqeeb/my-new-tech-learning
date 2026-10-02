# Python — Day 11 | 02 Oct 2026
# Topic: Functions

def greet(name):
    print("Welcome", name)

def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old")

def calculate_total(price, quantity):
    return price * quantity

def add_numbers(number1, number2):
    return number1 + number2

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def show_number(limit):
    for number in range(1, limit + 1):
        print(number)

def calculate_sum(limit):
    total = 0
    for number in range(1, limit + 1):
        total = total + number
    return total

def total_salary(salaries):
    total = 0
    for salary in salaries:
        total = total + salary
    return total

def high_salary(salary):
    if salary >= 50000:
        return "High"
    else:
        return "Normal"

def greet_user(name, country="Bangladesh"):
    print("Name:", name)
    print("Country:", country)

def calculate_bonus(salary, performance):
    if performance == "Good":
        return salary * 0.10
    else:
        return salary * 0.05

greet("Swaqeeb")
introduce("Tarin", 28)
print(calculate_total(300, 5))
print(add_numbers(40, 60))
print(check_age(25))
print(check_number(10))
show_number(5)
print(calculate_sum(5))
salaries = [30000, 45000, 25000, 50000]
print(total_salary(salaries))
print(high_salary(50000))
greet_user(country="Denmark", name="Tarin")
print(calculate_bonus(500000, "Good"))
print(calculate_bonus(500000, "Average"))
