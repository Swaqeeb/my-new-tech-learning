# Python — Day 20 | 11 November 2026

Topic: script-relative file paths and basic error handling.
Started 8 November; continued 9 and 11 November 2026. Notes finalized 11 November.

## 1. Find the script folder

```python
from pathlib import Path
script_folder = Path(__file__).resolve().parent
report_path = script_folder / "report.txt"
```

- `Path` comes from Python's built-in `pathlib` module.
- `__file__` identifies the Python script being run.
- `Path(__file__)` represents that location as a Path object.
- `.resolve()` makes the path absolute and resolves symbolic links.
- `.parent` gets the containing folder.
- `/` joins a Path object with a filename; here it is not numerical division.

For your script, `script_folder` points to:
`C:\Users\Dell\Projects\my-new-tech-learning\01_Basics\Day_20`

`report_path` points to `report.txt` inside that folder.
Building or printing a path does not create a file. Using this script-relative path also avoids depending on the terminal's current working folder.

## 2. Path, opened file, and contents

| Name | Meaning |
| --- | --- |
| `script_folder` | Folder containing the script |
| `report_path` | Full location of the report file |
| `file` | Opened file object used to read or write |
| `content` | Text returned by reading the file |

```python
with open(report_path, "r") as file:
    content = file.read()
    print(content)
```

`print(report_path)` displays the location. `print(content)` displays the text.
`with` closes the opened file when its block finishes, including when an exception occurs in the block.

## 3. File modes

| Mode | If the file exists | If the file is missing |
| --- | --- | --- |
| `"w"` | Immediately clears its contents, then allows writing | Creates it, provided the parent folder exists and access is allowed |
| `"a"` | Keeps existing contents and writes at the end | Creates it, provided the parent folder exists and access is allowed |
| `"r"` | Opens it for reading | Raises `FileNotFoundError` |

Mode letters are lowercase. `"W"` is invalid.

```python
with open(report_path, "w") as file:
    file.write("Day 20 IT Support Report")

with open(report_path, "a") as file:
    file.write("\nOpen tickets: 15")
```

`\n` starts a new line. `write()` does not automatically add one.
Running this whole script again leaves two lines because `"w"` resets the file before `"a"` adds the ticket line. Running only the append block repeatedly would add repeated ticket lines.

## 4. Variables versus literal text

```python
open(report_path, "r")                     # Uses the path stored in the variable
open(script_folder / "report.txt", "r")   # Same target file
open("report_path.txt", "r")              # Different, literal filename
```

Putting quotes around a variable name turns it into text. The literal relative filename is looked up from the current working folder, not automatically from the script folder.

## 5. Calling read()

```python
print(file.read())
```

The parentheses call the method. `file.read` refers to the method without running it, so printing it does not print the file's contents.
An existing empty file can be read successfully: `file.read()` returns `""`. An empty file is not a missing file.

## 6. Handle a missing file

```python
try:
    with open(report_path, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Please check the report location.")

print("Check completed.")
```

1. Python attempts the statements inside `try`.
2. If they succeed, it skips the `except` block.
3. If `FileNotFoundError` occurs, it skips the remaining statements in `try` and runs the matching `except` block.
4. After that handled error, execution continues after the entire block.

The final `print()` is not indented, so it is outside both blocks. It runs after a successful read or a handled missing-file error.
The handler does not create the missing file, restore erased contents, or prove that all code is correct. Other error types are not caught by this particular handler.

## 7. Mistakes corrected during practice

| Mistake | Correction and reason |
| --- | --- |
| Used a second `"w"` to add a ticket | Use `"a"` to preserve the heading |
| Expected a path assignment to create a file | A path is an address; opening in a suitable write mode creates the file |
| Used `"report_path"` or `"report_path.txt"` | Use the unquoted variable `report_path` |
| Tried reading from the path with `report_path.read()` | In this exercise, read from the opened object with `file.read()` |
| Used `file.read` | Add `()` to perform the read |
| Read before appending | Read after appending to display the latest contents |
| Printed the report twice | Two read-and-print blocks caused two displays; this did not prove duplicate file contents |
| Expected `print()` inside `except` to stop execution | Printing displays text; execution continues after the handled error |

## 8. Final practice file

Use `Day_20_Practice.py` alongside these notes. Keep `missing_report.txt` absent for the deliberate missing-file exercise. The script creates `report.txt` beside itself.

After the folder and report path messages, expected output is:

```text
Report file not found.
Missing-file exercise finished.
Day 20 IT Support Report
Open tickets: 15
Check completed.
```

The report itself contains only:

```text
Day 20 IT Support Report
Open tickets: 15
```

## 9. Learning checkpoint and next recall

- Guided practice completed for paths, file modes, read order, and missing-file handling.
- Both successful reading and missing-file handling were demonstrated in the user's output.
- Independently wrote the correct `try`/`except` structure and final print placement; needed correction from `file.read` to `file.read()`.
- Retention and fully independent execution still need a later recall check.
- GitHub commit/push for Day 20 is pending at the time of these notes.

Next session, without copying: build a script-relative report path, read it using `try`/`except FileNotFoundError`, and print a completion message after the block. Explain why an empty file does not trigger this handler and why a full rerun of this practice leaves two report lines.
