# Python — Day 3: September 12

## Topic: Conditional Statements

## Learning Objectives

Today I learned:

- What conditional statements are
- The `if` statement
- The `else` statement
- The `elif` statement
- Comparison operators
- The difference between `=` and `==`
- How Python makes decisions
- Indentation in Python
- Using `input()` with conditions
- Converting input using `int()`
- Creating real-world decision logic
- Basic troubleshooting of conditional statements

---

## 1. What Is a Conditional Statement?

A conditional statement allows Python to make a decision.

Python checks a condition.

If the condition is `True`, Python executes the code inside the block.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Because `20 >= 18` is `True`, Python prints:

```text
Adult
```

---

## 2. The `if` Statement

The basic structure is:

```python
if condition:
    # code to execute
```

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

The colon `:` is important.

The indented line belongs to the `if` statement.

---

## 3. Comparison Operators

Python uses comparison operators to compare values.

### Greater than

```python
>
```

Example:

```python
age > 18
```

### Less than

```python
<
```

Example:

```python
age < 18
```

### Greater than or equal to

```python
>=
```

Example:

```python
age >= 18
```

### Less than or equal to

```python
<=
```

Example:

```python
age <= 18
```

### Equal to

```python
==
```

Example:

```python
age == 20
```

### Not equal to

```python
!=
```

Example:

```python
age != 20
```

---

## 4. `=` vs `==`

This is an important Python concept.

### `=`

The single equal sign assigns a value to a variable.

Example:

```python
age = 20
```

This means:

**Store 20 in the variable `age`.**

### `==`

The double equal sign compares two values.

Example:

```python
age == 20
```

This asks:

**Is age equal to 20?**

The result is either:

```text
True
```

or:

```text
False
```

---

## 5. The `else` Statement

`else` runs when the `if` condition is `False`.

Example:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Not adult")
```

Output:

```text
Not adult
```

---

## 6. The `elif` Statement

`elif` means:

**else if**

It allows Python to check another condition when the previous condition was false.

Example:

```python
age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

Output:

```text
Teenager
```

---

## 7. Multiple Conditions

We can use `if`, `elif`, and `else` together.

Example:

```python
Marks = 85

if Marks >= 80:
    print("Excellent")
elif Marks >= 60:
    print("Good")
elif Marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Excellent
```

Python checks the conditions from top to bottom.

When it finds a condition that is `True`, it executes that block and skips the remaining conditions.

---

## 8. Using `input()` With Conditions

User input can be used to make decisions.

Example:

```python
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("Adult")
else:
    print("Not adult")
```

Because `input()` returns a string, we use:

```python
age = int(age)
```

before comparing the age with a number.

---

## 9. Real-World Age Classification

We can create multiple age categories.

```python
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

For an age of `34`, the output is:

```text
Adult
```

For an age of `15`, the output is:

```text
Teenager
```

---

## 10. Indentation

Python uses indentation to identify which code belongs to a conditional block.

Correct:

```python
if age >= 18:
    print("Adult")
```

The `print()` line is indented.

Incorrect indentation can cause an error.

Indentation is therefore part of Python syntax.

---

## 11. Python Interactive Shell

When entering a multi-line `if` statement in the interactive shell, Python automatically shows:

```text
...
```

The `...` means Python is waiting for the continuation of the block.

Do not type `...` yourself.

Example:

```text
>>> age = 20
>>> if age >= 18:
...     print("Adult")
...
Adult
```

After finishing the block, press Enter twice.

---

## 12. Errors I Encountered

### Error 1: Using `=` Instead of `==`

I learned that:

```python
=
```

is used for assignment.

While:

```python
==
```

is used for comparison.

### Error 2: Incorrect Indentation

Python requires the code inside an `if`, `elif`, or `else` block to be indented.

Correct:

```python
if age >= 18:
    print("Adult")
```

### Error 3: Typing `...` Manually

The Python shell displays `...` automatically for continuation lines.

I initially typed it manually.

Lesson:

**Do not type `...` yourself.**

### Error 4: Incorrect `else` Structure

`else` does not have its own condition.

Correct:

```python
if age >= 18:
    print("Adult")
else:
    print("Not adult")
```

---

## 13. Practice Completed

### Exercise 1 — Check if Someone Is an Adult

```python
age = 20

if age >= 18:
    print("Adult")
```

Output:

```text
Adult
```

Status: Completed.

### Exercise 2 — Check if Someone Is Not an Adult

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Not adult")
```

Output:

```text
Not adult
```

Status: Completed.

### Exercise 3 — Check for Exactly 20

```python
age = 20

if age == 20:
    print("Exactly 20")
```

Output:

```text
Exactly 20
```

Status: Completed.

### Exercise 4 — Age Classification

```python
age = 15

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

Output:

```text
Teenager
```

Status: Completed.

### Exercise 5 — Age Classification With User Input

```python
age = input("Enter your age: ")
age = int(age)

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

Tested with age 34.

Output:

```text
Adult
```

Status: Completed.

### Exercise 6 — Marks Classification

```python
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
```

Tested with marks 85.

Output:

```text
Excellent
```

Status: Completed.

---

## 14. Key Takeaways

1. Conditional statements allow Python to make decisions.
2. `if` checks a condition.
3. `elif` checks another condition when the previous condition is false.
4. `else` runs when all previous conditions are false.
5. `>` means greater than.
6. `<` means less than.
7. `>=` means greater than or equal to.
8. `<=` means less than or equal to.
9. `==` checks whether two values are equal.
10. `!=` checks whether two values are different.
11. `=` assigns a value to a variable.
12. Python uses indentation to define code blocks.
13. `input()` returns a string, so `int()` may be needed before numerical comparisons.
14. Conditions are checked from top to bottom.
15. The first matching `if` or `elif` block is executed.
16. `else` does not have a condition.
17. The Python shell displays `...` automatically for multi-line blocks.

---

## Day 3 Status

**Python — Day 3: September 12 — COMPLETED**

Next lesson:

**Python — Day 4**
