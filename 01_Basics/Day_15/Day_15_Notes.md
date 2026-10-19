# Python — Day 15 | 19 October 2026

**Core lesson status:** Completed (final banking challenge verified with output `Final Balance: 18000`).  
**Long-term mastery:** Not yet verified; spaced recall remains due.  
**Script status:** Prepared for full-file run; **not yet confirmed executed as a whole**.

## Learning objectives
- Explain **local variables**, **global variables**, and the `global` keyword.
- Pass arguments to functions and reuse functions with parameters.
- Distinguish `print()` from `return` and save returned values through assignment.
- Debug function syntax, indentation, spelling, case sensitivity, and variable-update mistakes.

## Local vs global
```python
team = "IT"  # global

def show_team():
    team = "Finance"  # separate local variable
    print("Inside:", team)

show_team()       # Inside: Finance
print(team)       # IT
```
A function may **read** a global variable without `global`. Assignment to a name inside a function normally creates a local binding. An assignment that also reads that uninitialized local variable can raise `UnboundLocalError`.

## `global` is for modifying a module-level binding
```python
open_tickets = 20

def resolve_tickets():
    global open_tickets
    open_tickets -= 5

resolve_tickets()
print(open_tickets)  # 15
```
`global` is **not** the same as `return`. Prefer parameters and returned values for reusable calculation functions.

## `return` versus `print()`
```python
def display_bonus(salary):
    print(salary + 5000)

def calculate_bonus(salary):
    return salary + 5000

x = display_bonus(30000)    # prints 35000; x is None
y = calculate_bonus(30000)  # y is 35000
```
Without an explicit `return`, a function returns `None`. After `return`, later statements in that function are not executed.

## Saving returned results
Calling a function alone does not update the caller's variable:
```python
balance = 10000

def withdraw(current_balance, amount):
    return current_balance - amount

withdraw(balance, 2000)            # discards returned 8000; balance stays 10000
balance = withdraw(balance, 2000)  # balance becomes 8000
```
Use distinct function parameters instead of relying on a particular global variable. This allows the same function to work for multiple accounts.

## Actual exercises and outputs from today's session
- Fixed a function definition that omitted parentheses and `:`.
- Moved statements out of the indented function body; `return` ends that function call.
- Withdrew 1500 from 5000: output **3500**, initially stored in separate `balnce` variable.
- Two withdrawals from 10000 (2000 then 1500): predicted **6500** correctly.
- Independently completed withdrawals 3000 and 2500 from 15000: output **9500**, after correcting invalid `return balance = ...` syntax.
- Independently reused `withdraw(current_balance, amount)` for A, B, C: outputs **21000**, **11500**, **6000**.
- Debugged `account_b-withdraw(...)` as a subtraction expression rather than assignment; changed to `account_b = withdraw(...)`.
- Correctly predicted a function with `print()` but no `return` results in an assigned `None`.
- Final challenge: start **20000**, deposit **5000**, withdraw **7000** → **18000**, after correcting case-sensitive names and using the updated balance.

## Common errors — personal revision list
| Error | Cause | Corrective habit |
|---|---|---|
| `def withdraw` or `def withdraw:` | Missing `()` and/or `:` | Write `def withdraw(amount):` |
| `NameError: New_Balance` | `New_balance` and `New_Balance` are different | Consistent spelling/case |
| `return balance = balance - amount` | Assignment is not valid after `return` | Use `return balance - amount` |
| `account_b-withdraw(...)` | Computes a difference, doesn't update variable | Use `account_b = withdraw(...)` |
| `print()` in place of `return` | Caller receives `None` | Return the desired result |
| Withdraw from old `balance` after deposit | Deposited value saved under another name | Pass and update the **latest** balance |

## Professional pattern
```python
def deposit(current_balance, amount):
    return current_balance + amount

def withdraw(current_balance, amount):
    return current_balance - amount

balance = 20000
balance = deposit(balance, 5000)
balance = withdraw(balance, 7000)
print("Final Balance:", balance)  # 18000
```
For a real banking system, additional checks and transaction safeguards are needed. These examples are basic learning exercises, not production banking code.

## Follow-up practice and retention
- **Next session:** Independent problem using `return` with no template; identify whether the returned result was assigned.
- **After ~3 days and ~7 days:** Revisit function scope, `global`, assignment, and `print()` versus `return` with unseen problems.
- **Unattempted challenge:** Write reusable deposit and withdraw functions, process a salary adjustment or bank transactions, then debug one intentionally broken function.
- Record: *core lesson completed*, not *long-term mastery certified*.
