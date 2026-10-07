# Python — Day 14 | 07 Oct 2026

## Status
COMPLETED

## Topic
Function Arguments: Default Parameters, Positional/Keyword Arguments, `*args`, and `**kwargs`

## 1. Default Parameters
A default parameter is used when the caller does not provide that argument.

```python
def greet(name="Guest"):
    print("Hello", name)

greet("Swaqeeb")
greet()
```

Key idea:
- Provided argument → Python uses the provided value.
- Missing argument → Python uses the default value.

## 2. Positional and Keyword Arguments

```python
def employee_info(name, department, location):
    print(name, department, location)

employee_info("Rahim", "Finance", "Chattogram")
employee_info(location="Chattogram", name="Rahim", department="Finance")
```

Key ideas:
- Positional arguments are matched from left to right.
- Keyword arguments are matched by parameter name.
- When mixing them, positional arguments come before keyword arguments.
- Python is case-sensitive.

Important error learned:

```text
SyntaxError: positional argument follows keyword argument
```

Another error learned:

```text
TypeError: ... got multiple values for argument 'name'
```

This happens when the same parameter receives a value both positionally and by keyword.

## 3. `*args`
`*args` collects any number of positional arguments into a tuple.
The name after `*` can be descriptive, such as `*numbers`.

```python
def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    print(total)

add_numbers(34, 56, 54)
```

Output:

```text
144
```

Independent six-number test:

```python
add_numbers(34, 56, 54, 456, 54, 344)
```

Output:

```text
998
```

Use `*args` when the number of positional values is not known beforehand.

## 4. `**kwargs`
`**kwargs` collects any number of keyword arguments into a dictionary.
The name after `**` can be descriptive, such as `**details`.

```python
def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)
```

Example:

```python
student_details(name="alok", course="Higher Math", city="Dhaka", age=34)
```

Key idea:
- `*args` → tuple
- `**kwargs` → dictionary

Dictionary values can be accessed directly:

```python
details["name"]
details["course"]
```

Or all key/value pairs can be processed with:

```python
for key, value in details.items():
    print(key, value)
```

## Final Challenge
Created `employee_details(**details)`, looped through `details.items()`, and printed four independently supplied keyword values:
- name
- department
- location
- salary

Final output:

```text
name moonim
department logic
location Dhaka
salary 500000
```

## Common Errors Corrected
- Used `:` instead of `=` in a keyword argument.
- Put a positional argument after a keyword argument.
- Passed two values to the same parameter.
- Used incorrect capitalization for a parameter name.
- Typed `locaiton` instead of `location`.
- Typed `salaray` instead of `salary`.
- Printed literal text such as `"name"` instead of retrieving `details["name"]`.
- Missed a closing parenthesis while defining a function.

## Memory Rules
- Positional arguments fill parameters from left to right.
- Keyword arguments name the target parameter directly.
- Positional arguments come before keyword arguments when mixed.
- `*args` collects positional arguments into a tuple.
- `**kwargs` collects keyword arguments into a dictionary.
- `.items()` gives both the key and value from a dictionary.

## Next
Python Day 15.
