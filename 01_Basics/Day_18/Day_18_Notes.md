# Python — Day 18 | 04 November 2026

**Lesson status:** Coding and final challenge verified in chat. **Independent mastery:** continuing; some syntax corrections were required.  
**Focus:** Dictionary operations, nested dictionaries, lists of dictionaries, searching and updating IT records.

## Previously learned — brief recall
- A dictionary stores key–value pairs, e.g. `employee["department"]`.
- `.items()` lets a loop receive each key and value.
- Day 14 had already introduced dictionaries with `**kwargs`; these are **not** new Day 18 concepts.

## New and extended practice

### Read, update and add dictionary values
```python
employee = {"name": "Karim", "location": "Dhaka", "status": "Active"}
print(employee["name"])               # Karim
employee["location"] = "Chattogram" # update existing key
employee["employee_id"] = 105        # add a new key
```
Use a *key*, not a numerical list index, to retrieve a dictionary value.

### Delete with `del`, and remove + return with `.pop()`
```python
del employee["employee_id"]
removed_status = employee.pop("status")
print(removed_status)                  # Active
```
Both operations can raise `KeyError` if the key is missing. `.pop("status", "Unknown")` can instead supply a fallback.

### Safe retrieval with `.get()`
```python
device = {"asset_id": 501, "type": "Laptop"}
print("Device location:", device.get("location", "Unknown"))
# Device location: Unknown
device["location"] = "Dhaka"
print("Device location:", device.get("location", "Unknown"))
# Device location: Dhaka
```
The printed label belongs outside the lookup; `"location"` is the key, `"Unknown"` is the fallback value.

### Nested dictionaries
```python
laptop = {"asset_id": 510, "owner": {"name": "Karim", "department": "Finance", "location": "Dhaka"}, "status": "Active"}
print(laptop["owner"]["name"])
laptop["owner"]["department"] = "IT"
```
A chained lookup accesses an inner dictionary, then one of its keys.

### Lists of dictionaries
```python
tickets = [{"id": 1001, "status": "Open"}, {"id": 5656, "status": "Pending"}]
print(tickets[1]["status"])  # Pending
```
**List position is not a ticket ID.** Use a loop to search by ID rather than guessing the index. For millions of records, a dictionary keyed by ID or an indexed database is preferable to scanning a list repeatedly.

### Search using `for...else`
```python
for ticket in tickets:
    if ticket["id"] == 5656:
        print("Ticket 5656 Status:", ticket["status"])
        break
else:
    print("Ticket not found")
```
The `else` under `for` executes only if the loop ends **without** `break`. A `found = False` flag is an alternative, but unnecessary in this particular structure.

### Final challenge — verified
```python
tickets = [
    {"id": 101, "status": "Open"},
    {"id": 102, "status": "Pending"},
    {"id": 103, "status": "Resolved"},
]
for ticket in tickets:
    if ticket["id"] == 102:
        ticket["status"] = "Resolved"
        print("Ticket 102 updated successfully")
        break
else:
    print("Ticket not found")
print(tickets[1])
```
Verified output:
```text
Ticket 102 updated successfully
{'id': 102, 'status': 'Resolved'}
```

## Debugging and syntax-recall log
1. `device["status"] = "Inactive"` updates; `del device["temporary_ip"]` deletes (do not use `=` with `del`).
2. `ticket["id"]` retrieves the ID value; `"id" == 5656` compares unlike values and is always false.
3. Use `ticket["status"]`, including quotation marks around the key; `ticket[status]` interprets `status` as a variable.
4. In `for ticket in tickets`, `ticket` is one dictionary, while `tickets` is the whole list.
5. Perform a matched update **before** `break`; change `ticket["status"]`, not `ticket["id"]`.
6. A final verification `print(tickets[1])` goes **outside** the `for...else` block.
7. Prefer independent first attempts, then notes, then a later no-hint recheck. Reviewing notes during learning is valid; it is not proof of memorized syntax.
8. VS Code runs the entire `.py` file top to bottom; earlier exercises may contribute extra output.

## Verification and storage status
- The final ticket update was verified via the user's VS Code output on 04 Nov 2026.
- `Day_18_Notes.md` is a prepared lesson record.
- A separate `Day_18_Reference_Practice.py` is **reconstructed from chat**, not the user's full local `Day_18_Practice.py`.
- Google Drive storage and GitHub synchronization are tracked independently; do not mark GitHub pushed until actual `git push` output is received.

## Next lesson / recall
- Begin Day 19 with brief no-hint retrieval of `del`, `.pop()`, `.get()` and `ticket["status"]`.
- Then advance to a new topic, avoiding another whole day of repeated list/dictionary fundamentals.
