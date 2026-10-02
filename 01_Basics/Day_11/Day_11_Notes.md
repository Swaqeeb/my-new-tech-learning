# Python --- Day 11 \| 02 Oct 2026

## Topic: Functions

## What I learned

-   Defining and calling functions with `def`.
-   Parameters and arguments, including multiple parameters.
-   `print()` versus `return`.
-   Local variables and variable scope.
-   Functions with `if`, `elif`, and `else`.
-   Functions with `for` loops and accumulators.
-   Functions that receive lists.
-   Default parameters and keyword arguments.
-   Testing boundary values such as `>= 50000`.
-   Writing reusable functions instead of fixed solutions.

## Key practice

``` python
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

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

def greet_user(name, country="Bangladesh"):
    print("Name:", name)
    print("Country:", country)
```

## Final challenge

``` python
def calculate_bonus(salary, performance):
    if performance == "Good":
        return salary * 0.10
    else:
        return salary * 0.05

print(calculate_bonus(500000, "Good"))
print(calculate_bonus(500000, "Average"))
```

Output:

``` text
50000.0
25000.0
```

## Errors I learned from

-   Misspelled function names can cause `NameError`.
-   Missing `:` and incorrect indentation cause syntax/indentation
    errors.
-   `elif` must come before `else` and must have a condition.
-   Local variables cannot normally be accessed outside their function.
-   Putting `return` inside a loop can end the function too early.
-   A missing return path can produce `None`.
-   `return bonus = ...` is invalid syntax.
-   In the interactive shell, Python supplies the `...` prompt
    automatically.

## Status

COMPLETED
