# Python — Day 13 | 06 Oct 2026

## Topic: String Validation Methods

### New methods learned

- `.isdigit()` — True when the string contains only digits.
- `.isalpha()` — True when the string contains only letters.
- `.isalnum()` — True when the string contains only letters and/or digits.
- `.isspace()` — True when the string contains only whitespace and is not empty.
- `.islower()` — checks whether cased letters are lowercase.
- `.isupper()` — checks whether cased letters are uppercase.
- `.istitle()` — checks whether text uses title-style capitalization.
- `.title()` — converts text to title-style capitalization.

## Important review from earlier days

- `.strip()` removes surrounding whitespace.
- `.replace(old, new)` replaces matching text.
- String methods must normally be called with parentheses, e.g. `code.islower()` rather than `code.islower`.
- `if` and `else` lines end with a colon `:` and their bodies must be indented.

## Practice examples

```python
age = input("Enter your age: ")
if age.isdigit():
    print("Valid age")
else:
    print("Invalid age")
```

```python
name = "Tarin Islam"
clean_name = name.replace(" ", "")
print(clean_name.isalpha())
```

```python
username = input("Enter username: ")
if username.isalnum():
    print("Valid username")
else:
    print("Invalid username")
```

```python
message = input("Enter a message: ")
if message.strip() == "":
    print("Empty message")
else:
    print("Message received")
```

```python
name = "swaqeeb islam"
new_name = name.title()
print(new_name.istitle())
```

## Final challenge

```python
username = "  Swaqeeb123 "
clean_username = username.strip()

if clean_username.isalnum():
    print("Valid username")
else:
    print("Invalid username")
```

Output:

```text
Valid username
```

## Recurring errors to review

- Using `;` instead of `:` after `if`.
- Forgetting parentheses when calling a method, e.g. `code.islower` instead of `code.islower()`.
- Misspelling methods such as `isalnum()`.
- Remember that `.replace()` needs at least the old text and new text.
- A method result does not automatically change the original string unless it is assigned.

## Retention note

The goal is not to memorize every method immediately. Future lessons should start with short situation-based recall exercises and recycle methods from Days 12–13 until method selection becomes natural.

## Status

COMPLETED
