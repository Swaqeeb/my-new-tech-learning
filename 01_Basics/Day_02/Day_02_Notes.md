# Python — Day 2: September 11

## Topic: User Input and Type Conversion

## Learning Objectives

Today I learned:

- What `input()` does
- How Python receives user input
- That `input()` returns a string
- What `int()` does
- What `float()` does
- Difference between integers and floats
- Converting user input into numbers
- Using converted values in calculations
- Using multiple inputs
- Printing variables and results
- Understanding `TypeError`
- Basic troubleshooting in the Python interactive shell

---

## 1. The `input()` Function

The `input()` function allows Python to receive information from the user.

Example:

```python
name = input("Enter your name: ")
print(name)
```

When Python reaches `input()`, it waits for the user to type something.

---

## 2. `input()` Returns a String

An important rule:

**`input()` always returns a string (`str`).**

Example:

```python
price = input("Enter the price: ")
print(type(price))
```

If the user enters:

```text
25.50
```

Python treats it as:

```python
"25.50"
```

The type is:

```text
<class 'str'>
```

Even if the user enters a number, `input()` initially treats it as text.

---

## 3. Converting Input to a Float

If we need a decimal number, we can use `float()`.

Example:

```python
price = input("Enter the price: ")
price = float(price)

print(price)
print(type(price))
```

If the user enters `25.50`, Python converts it to a float.

---

## 4. Converting Input to an Integer

If we need a whole number, we can use `int()`.

Example:

```python
quantity = input("Enter quantity: ")
quantity = int(quantity)

print(quantity)
print(type(quantity))
```

If the user enters `2`, Python converts the string `"2"` into the integer `2`.

---

## 5. Integer vs Float

An integer is a whole number.

Examples:

```python
10
25
100
```

A float is a number that can contain a decimal value.

Examples:

```python
10.5
25.50
100.75
```

Example:

```python
age = 34
price = 25.50
```

Here `age` is an integer and `price` is a float.

---

## 6. Using Converted Values in Calculations

We can convert user input and then use it in calculations.

Example:

```python
price = input("Enter price: ")
price = float(price)

quantity = input("Enter quantity: ")
quantity = int(quantity)

total = price * quantity

print(total)
```

If the user enters price `50` and quantity `2`, the output is:

```text
100.0
```

---

## 7. Multiple Inputs

Python can receive several pieces of information from the user.

Example:

```python
product = input("Enter product name: ")

price = input("Enter price: ")
price = float(price)

quantity = input("Enter quantity: ")
quantity = int(quantity)

total = price * quantity

print("Product", product)
print("Total:", total)
```

Example input:

```text
Laptop
5000
2
```

Output:

```text
Product Laptop
Total: 10000.0
```

---

## 8. Why Type Conversion Is Important

Suppose we write:

```python
price = input("Enter price: ")
quantity = input("Enter quantity: ")

total = price * quantity
```

Both values are strings.

Python cannot perform the numerical calculation we want because the values have not been converted into numbers.

We should use:

```python
price = float(price)
quantity = int(quantity)
```

before performing the calculation.

---

## 9. Common Type Conversion Functions

### `int()`

Converts a value into an integer when possible.

Example:

```python
number = int("25")
print(number)
```

Output:

```text
25
```

### `float()`

Converts a value into a floating-point number.

Example:

```python
number = float("25.50")
print(number)
```

Output:

```text
25.5
```

### `str()`

Converts a value into a string.

Example:

```python
number = str(25)
print(number)
print(type(number))
```

Output:

```text
25
<class 'str'>
```

---

## 10. Understanding `TypeError`

A `TypeError` can happen when Python receives a type of value that cannot be used for an operation.

For example, if we accidentally try to perform a numerical calculation using strings instead of numbers, Python may produce a `TypeError`.

The important lesson is:

**Check the data type before performing calculations.**

Useful command:

```python
print(type(variable))
```

---

## 11. Interactive Shell Troubleshooting

When working in the Python interactive shell, old variables can remain in memory.

This can sometimes cause confusing results.

If the shell becomes confusing, restarting the Python shell gives a clean environment.

Important lesson:

**Always check the current value and type of a variable when troubleshooting.**

Example:

```python
print(variable)
print(type(variable))
```

---

## 12. Errors I Encountered

### Error 1: Using Input Directly for Calculation

I learned that `input()` returns a string.

Solution:

```python
price = float(price)
```

or:

```python
quantity = int(quantity)
```

depending on the required type.

### Error 2: Confusion Between Integer and Float

Whole numbers use `int`.

Decimal numbers use `float`.

Example:

```python
quantity = int(quantity)
price = float(price)
```

### Error 3: Old Variables in the Interactive Shell

Previously created variables can remain available in the interactive shell.

This can sometimes cause unexpected results.

Solution:

Restart the Python shell when necessary and run the code again from the beginning.

---

## 13. Practice Completed

### Exercise 1 — Check the Type of User Input

```python
price = input("Enter the price: ")
print(type(price))
```

Tested with `25.50`.

Result:

```text
<class 'str'>
```

Status: Completed.

### Exercise 2 — Convert Price to Float

```python
price = input("Enter the price: ")
price = float(price)

print(price)
print(type(price))
```

Status: Completed.

### Exercise 3 — Convert Quantity to Integer

```python
quantity = input("Enter quantity: ")
quantity = int(quantity)

print(quantity)
print(type(quantity))
```

Status: Completed.

### Exercise 4 — Calculate Total Price

```python
price = input("Enter price: ")
price = float(price)

quantity = input("Enter quantity: ")
quantity = int(quantity)

total = price * quantity

print(total)
```

Status: Completed.

### Exercise 5 — Product and Total

```python
product = input("Enter product name: ")

price = input("Enter price: ")
price = float(price)

quantity = input("Enter quantity: ")
quantity = int(quantity)

total = price * quantity

print("Product", product)
print("Total:", total)
```

Tested with a Laptop, price 5000, quantity 2.

Output:

```text
Product Laptop
Total: 10000.0
```

Status: Completed.

---

## 14. Key Takeaways

1. `input()` allows Python to receive information from the user.
2. `input()` always returns a string.
3. `int()` converts suitable values into integers.
4. `float()` converts suitable values into floating-point numbers.
5. `str()` converts values into strings.
6. Use `int()` for whole-number input such as quantity.
7. Use `float()` for decimal input such as price.
8. Convert input before using it in numerical calculations.
9. `type()` can be used to check the type of a value.
10. Old variables can remain in the interactive shell.
11. Restarting the shell can help when troubleshooting confusing variable states.
12. Understanding data types helps prevent calculation errors.

---

## Day 2 Status

**Python — Day 2: September 11 — COMPLETED**

Next lesson:

**Python — Day 3**
