# Python — Day 2: September 11
# Topic: User input and type conversion

# ============================================================
# Exercise 1: Check the type of user input
# ============================================================

price = input("Enter the price: ")
print(type(price))

# Example:
# If the user enters 25.50:
# <class 'str'>


# ============================================================
# Exercise 2: Convert price to float
# ============================================================

price = input("Enter the price: ")
price = float(price)

print(price)
print(type(price))

# Example:
# If the user enters 25.50:
# 25.5
# <class 'float'>


# ============================================================
# Exercise 3: Convert quantity to integer
# ============================================================

quantity = input("Enter quantity: ")
quantity = int(quantity)

print(quantity)
print(type(quantity))

# Example:
# If the user enters 2:
# 2
# <class 'int'>


# ============================================================
# Exercise 4: Calculate total price
# ============================================================

price = input("Enter price: ")
price = float(price)

quantity = input("Enter quantity: ")
quantity = int(quantity)

total = price * quantity

print(total)

# Example:
# Price: 50
# Quantity: 2
# Output:
# 100.0


# ============================================================
# Exercise 5: Product and total
# ============================================================

product = input("Enter product name: ")

price = input("Enter price: ")
price = float(price)

quantity = input("Enter quantity: ")
quantity = int(quantity)

total = price * quantity

print("Product", product)
print("Total:", total)

# Example:
# Product: Laptop
# Price: 5000
# Quantity: 2
# Output:
# Product Laptop
# Total: 10000.0


# ============================================================
# Day 2 key lessons
# ============================================================
# 1. input() receives information from the user.
# 2. input() returns a string.
# 3. int() converts suitable values into integers.
# 4. float() converts suitable values into floating-point numbers.
# 5. str() converts values into strings.
# 6. Convert input before using it in numerical calculations.
# 7. Use int() for whole-number input such as quantity.
# 8. Use float() for decimal input such as price.
# 9. type() can be used to check the data type.
# 10. Old variables can remain in the interactive shell.
# 11. Restarting the shell can help with confusing variable states.
