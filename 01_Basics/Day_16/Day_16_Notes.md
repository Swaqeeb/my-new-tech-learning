# Python — Day 16 | 02 November 2026

**Status:** List mastery / spaced-revision session completed. Saved script and GitHub sync pending user verification.

## Curriculum check
Earlier Python Day 7 already covered lists: indexing, changing items, len(), loops, accumulators, and `for` + `if`. Day 8 covered collections and loops. Later function exercises combined loops and lists. Therefore Day 16 is **revision and strengthening**, not the introduction of lists or list methods.

## Concepts revised
- Positive indexes start at `0`; negative indexes count from the end (`-1` is last).
- Invalid indexes raise `IndexError`, not an empty result.
- Assignment `items[index] = value` **replaces** an existing element.
- `.append(value)` adds one item at the end.
- `.insert(index, value)` inserts and shifts later positions.
- `.remove(value)` deletes the **first matching value**; a missing value raises `ValueError`.
- `.pop()` deletes and returns the last item; `.pop(index)` deletes and returns the indexed item.
- Calling `.pop()` twice removes two elements, even when the first result was not assigned.
- Strings and variable names must be spelled consistently; Python is case-sensitive.

## Verified practice from user's Python terminal
### Device inventory — all operations in sequence
```python
devices = ["Laptop", "Printer", "Router", "Monitor"]
devices.append("Firewall")
devices.insert(2, "Switch")
devices.remove("Printer")
removed_device = devices.pop()
print("Final inventory:", devices)
print("Removed device:", removed_device)
```
Expected and user-verified result:
```
Final inventory: ['Laptop', 'Switch', 'Router', 'Monitor']
Removed device: Firewall
```

### Ticket inventory — transfer to a new scenario
```python
tickets = [101, 102, 103, 104]
tickets.append(105)
tickets.insert(0, 999)
tickets.remove(102)
closed_ticket = tickets.pop()
print("Remaining:", tickets)
print("Closed ticket Number:", closed_ticket)
```
Result for remaining tickets verified as `[999, 101, 103, 104]`. The saved `closed_ticket` is `105` by program logic; the pasted final terminal output was truncated.

### Pop by index
```python
tickets = [101, 102, 103]
closed_ticket = tickets.pop(1)
print(closed_ticket)  # 102
print(tickets)        # [101, 103]
```
Learner correctly predicted both outputs.

## Error log / review targets
1. Insertion shifts later indexes; keep track of new positions after each change.
2. `.remove()` removes only the first match, not all duplicates.
3. Avoid accidental double `.pop()`.
4. Case sensitivity: `Closed_ticket` and `closed_ticket` differ; method name `.insert`, not `.incert`.
5. Read the complete multi-step task and execute each required operation in order.
6. Spell literal strings accurately (`Printer`, `Desktop`).

## New learning strategy
After a break, start with recall without hints; practice easy → medium → complex, debug independently, and use fresh workplace scenarios. Recheck retention at approximately 1, 3 and 7 days. Do not mark mastery as retained until new tasks are solved again without hints.

## Follow-up challenge (not attempted; leave pending)
Use a list of ticket IDs plus a `for` loop, `if`, and a function to identify and summarize tickets satisfying a condition. These combinations were introduced in earlier lessons; use them in *new, more realistic* exercises rather than labelling them first-time concepts.
