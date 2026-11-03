# Python — Day 17 | 03 November 2026

## Status
- Core lesson and seven exercises completed; final script executed successfully in VS Code.
- Topic: revision of lists, `for` loops, `if` conditions, counters, and sums; application of functions, configurable thresholds, and multiple return values.
- VS Code skills: open a project folder, restore the Explorer pane, create folders and `.py` files, save with Ctrl+S, run in the integrated PowerShell terminal, and use Run Python File.
- Practice file on the learner's Windows PC: `01_Basics/Day_17/Day_17_Practice.py`.
- Day 17 GitHub commit/push: not yet verified.

## Key concepts

### Loop over a list
```python
laptops = [201, 202, 203, 204, 205]
for laptop in laptops:
    print('Laptop ID:', laptop)
```
`laptops` is the complete list; `laptop` is the current item.

### Filter, count, and sum
```python
open_tickets = [7, 14, 3, 21, 12, 5, 18]
count = 0
total_tickets = 0
for ticket in open_tickets:
    if ticket > 10:
        count = count + 1
        total_tickets = total_tickets + ticket
print('Employees with high workload:', count)  # 4
print('Total high-workload tickets:', total_tickets)  # 65
```
Initialize accumulators before the loop. Print outside the loop for a single final result. `count + 1` counts matching employees; `total_tickets + ticket` sums ticket quantities.

### Reusable function with threshold
```python
def calculate_high_workload(open_tickets, threshold):
    total = 0
    for ticket in open_tickets:
        if ticket > threshold:
            total += ticket
    return total

team_b = [6, 14, 9, 25, 12]
print(calculate_high_workload(team_b, 15))  # 25
print(calculate_high_workload(team_b, 10))  # 51
print(calculate_high_workload(team_b, 20))  # 25
```
A parameter lets the same function work with multiple teams and rules.

### Return two results
```python
def analyze_workload(open_tickets):
    count = 0
    total = 0
    for ticket in open_tickets:
        if ticket > 10:
            count += 1
            total += ticket
    return count, total

team_c = [8, 16, 4, 23, 12, 7]
employees, total_tickets = analyze_workload(team_c)
print('Employees with high workload:', employees)  # 3
print('Total high-workload tickets:', total_tickets)  # 51
```
`return count, total` returns a tuple, unpacked into `employees` and `total_tickets`. `return` must be after the `for` loop so all tickets are examined.

## Debugging lessons from today's work
1. `for ticket in items:` uses `in`, not `on`.
2. Python is case-sensitive: `Open_tickets` differs from `open_tickets`. Mismatched names can accidentally reference an older global variable.
3. Spell identifiers consistently: `tickests` and `tickets` are different; the terminal may retain previously defined variables.
4. `print(laptops)` prints the whole list; `print(laptop)` prints the current item.
5. Printing inside a loop repeats output; a final summary should be printed after the loop.
6. Do not return from inside the `if` or `for` loop if the function must examine every item.
7. A function-local `count` is different from an outside `count`. Print the returned value rather than a stale global variable.
8. In VS Code's `.py` editor, never type REPL prompts `>>>` or `...`.
9. Correct output spelling: `workload`, `priority`, `employees` (plural where applicable).

## Verified exercise results
- Loop through laptops: 201, 202, 203, 204, 205.
- Filter IDs above 203: 204, 205.
- Filter ticket IDs above 200: 250, 400, 310.
- Count employees with >10 open tickets in `[5,12,3,18,7,15]`: 3.
- Filter `[8,15,4,22,11,6]`: 15, 22, 11; count 3; ticket sum 48.
- Combined count/sum `[7,14,3,21,12,5,18]`: 4 employees, 65 tickets.
- Function count with `[5,12,18,3,20]`: 3.
- Function sum with `[6,14,9,25,12]`: 51 (>10); 25 (>15); 25 (>20).
- Two-return-value function with `[8,16,4,23,12,7]`: `(3, 51)`; unpacked and displayed correctly.

## Follow-up for mastery
- **Next session:** independently implement a function that returns count, sum, and matching ticket IDs for a configurable threshold, without copying existing code.
- Revisit the `return` indentation, local versus global variables, and variable spelling after 1, 3, and 7 days.
- Save verified Day 17 script and notes in Google Drive and GitHub; GitHub synchronization is pending.
