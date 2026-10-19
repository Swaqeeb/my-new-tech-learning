"""Python — Day 15 | 19 October 2026
Local/global scope, global keyword, parameters, return, print vs return.
The runnable demonstrations below follow the verified lesson exercises.
"""

# 1. Local and global variables with identical names
team = "IT"
def show_team():
    team = "Finance"  # local variable
    print("Inside:", team)
show_team()
print("Outside:", team)  # global team remains IT

# 2. Updating a global value (learning example)
open_tickets = 20
def resolve_tickets():
    global open_tickets
    open_tickets = open_tickets - 5
resolve_tickets()
print("Remaining tickets:", open_tickets)  # 15

# 3. Prefer a reusable function with parameters and return
def withdraw(current_balance, amount):
    return current_balance - amount

account_a = 25000
account_b = 15000
account_c = 8000
account_a = withdraw(account_a, 4000)
account_b = withdraw(account_b, 3500)
account_c = withdraw(account_c, 2000)
print("Account A:", account_a)  # 21000
print("Account B:", account_b)  # 11500
print("Account C:", account_c)  # 6000

# 4. print displays a value; return supplies a reusable value
def display_bonus(salary):
    print(salary + 5000)

def calculate_bonus(salary):
    return salary + 5000

print("No explicit return:", display_bonus(30000))  # 35000, then None
print("Returned value:", calculate_bonus(30000))   # 35000

# 5. Final verified deposit + withdrawal exercise
def deposit(current_balance, amount):
    return current_balance + amount

balance = 20000
balance = deposit(balance, 5000)
balance = withdraw(balance, 7000)
print("Final Balance:", balance)  # 18000

# === Independent retention exercises (NOT YET COMPLETED) ===
# A. Starting with 80000, add a bonus of 12000, then deduct 6500.
#    Use functions and return; do not use global.
# B. Debug a function that prints its calculation but returns None.
# C. After a break, predict local/global values before executing any code.
# D. Optional future improvement: reject withdrawals larger than the balance.
