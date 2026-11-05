# Python — Day 19 | 05 November 2026

**Topic:** File handling in Python — create, write, read, append, search, and count text-file entries  
**Coding lesson:** Completed based on code and terminal outputs shared in chat.  
**Long-term mastery:** Not yet independently verified.  
**Original local files:** Confirmed present by learner; not uploaded or inspected directly in this chat.

## 1. Files and working directory

Local learning folder: `01_Basics/Day_19/`

Confirmed local files:
- `Day_19_Practice.py`
- `Day_19_Append_Practice.py`
- `Day_19_Read_Lines.py`
- `report.txt`

Running a Python script from VS Code can use the project root as its current working directory. The learner checked:

```python
import os
print(os.getcwd())
```

Output: `C:\Users\Dell\Projects\my-new-tech-learning`.

A relative filename such as `report.txt` therefore created the file in the project root. To target the Day 19 folder while running from that root, use `01_Basics/Day_19/report.txt`.

## 2. Writing files with `w`

```python
with open("01_Basics/Day_19/report.txt", "w") as file:
    file.write("IT Support Report")
```

- `w` creates a file if missing and **overwrites** existing content if present.
- `with` automatically closes the file.
- `file.write(...)` writes a string, but does not automatically add a newline.
- The program may print nothing while successfully writing a file.

## 3. Reading files with `r`

```python
with open("01_Basics/Day_19/report.txt", "r") as file:
    content = file.read()
print(content)
```

- `r` reads an existing file.
- `.read()` loads its entire text into a string.
- A missing file path causes `FileNotFoundError`.

## 4. Appending files with `a`

```python
with open("01_Basics/Day_19/report.txt", "a") as file:
    file.write("\nTotal Open Tickets: 15")
```

- `a` preserves existing content and writes at the end.
- `\n` starts a new line.
- Re-running an append operation adds duplicate lines unless the script checks first.
- Avoid running an earlier `w` block in the same script before testing persistence across executions.

## 5. Preventing repeated entries

```python
report_path = "01_Basics/Day_19/report.txt"
new_entry = "Resolved Tickets: 8"

with open(report_path, "r") as file:
    content = file.read()

if new_entry in content:
    print("Entry already exists")
else:
    with open(report_path, "a") as file:
        file.write("\n" + new_entry)
    print("Entry Added")
```

**Learner verification:** A line containing `Resolved Tickets: 8` was confirmed once after repeated runs. Later output from the local report showed `Total Open Tickets: 8` instead; this difference is recorded rather than silently reconciled. This simple substring check is appropriate for a lesson; in production, exact line matching and normalized structured data are safer.

**Important mistake:** `file.write("\nnew_entry")` and `file.write("\n" + "new_entry")` write literal text, not the variable. Use `file.write("\n" + new_entry)`.

## 6. Reading file lines

```python
with open(report_path, "r") as file:
    for line in file:
        print(line.strip())
```

A `for` loop over the **file** yields lines; a `for` loop over a **string** yields characters. `.strip()` removes surrounding whitespace and trailing newline characters when displaying text.

## 7. Counting report lines

```python
count = 0
with open(report_path, "r") as file:
    for line in file:
        count = count + 1
print("Total report lines:", count)
```

Learner-confirmed result: **4** lines.

## 8. Counting ticket-related lines without case sensitivity

```python
count = 0
with open(report_path, "r") as file:
    for line in file:
        if "tickets" in line.lower():
            count = count + 1
print("Total tickets related lines:", count)
```

Learner-confirmed result: **3** matching lines. `line.lower()` normalizes the file line to lowercase, so the search literal must also be lowercase.

## 9. Searching using `for ... else`

```python
search_text = "Resolved Tickets: 8"
with open(report_path, "r") as file:
    for line in file:
        if search_text.lower() in line.lower():
            print("Entry found")
            break
    else:
        print("Entry not found")
```

Learner-confirmed output for the report at that stage: **Entry not found**. Here, `else` aligns with the `for`, and runs only if the search loop completes without `break`.

## 10. Errors corrected and retention targets

- Misspelled folder paths: `01_Basic` instead of `01_Basics`; `Day_09` instead of `Day_19`.
- Confused a string literal (`"new_entry"`) with the variable (`new_entry`).
- Put `print("Entry Added")` outside `else`, giving a misleading success message.
- Iterated over `line` rather than the file, counting characters instead of lines.
- Printed `line` rather than `count` during line counting.
- Mixed `"Tickets"` and lowercase `line.lower()`, causing zero matches.
- Required practice aligning `else` with `for` for correct not-found behavior.
- Typographical output labels and inconsistent capitalization in text-file report.

## 11. Session status and next lesson

**Day 19 coding:** Completed; verified through user-provided code, outputs, and file-presence confirmation.  
**Original files:** Saved locally; Google Drive upload and GitHub synchronization are separate pending steps.  
**Next Python day:** Improve reliable file paths (`pathlib`), exception handling (`FileNotFoundError`), and/or structured ticket records stored in files, after brief no-hint recall.

**Retention check:** Rebuild a short write/read/append/search program from memory on a later day; distinguish exercise completion from independent mastery.
