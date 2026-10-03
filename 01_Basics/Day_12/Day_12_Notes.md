# Python --- Day 12 \| 03 Oct 2026

**Status:** COMPLETED\
**Topic:** Built-in Functions & Useful String Methods

## Concepts Learned

-   `len()` --- get the length of a string or collection.
-   `.upper()` --- convert text to uppercase.
-   `.lower()` --- convert text to lowercase.
-   `.strip()` --- remove unwanted whitespace from the beginning and
    end.
-   `.replace(old, new)` --- replace matching text.
-   `.split()` --- split one string into a list; a custom separator such
    as `","` can be supplied.
-   `.find()` --- return the starting index of matching text; returns
    `-1` when not found.
-   `.count()` --- count how many times text appears.
-   `.startswith()` --- check whether text begins with a value.
-   `.endswith()` --- check whether text ends with a value.
-   `.join()` --- combine a list of strings into one string using a
    separator.
-   `isinstance(value, type)` --- check whether a value is a particular
    data type.

## Important Connections

-   `.strip()` → remove outside spaces.
-   `.split()` → one string → list of pieces.
-   `.join()` → list of strings → one string.
-   `.find()` → WHERE is it?
-   `.count()` → HOW MANY?
-   `.startswith()` → check the beginning.
-   `.endswith()` → check the end.

## Combined Practice

Used comma-separated text with `.split(",")`, looped through the
resulting list, and applied `.strip()` to each individual string.

Important distinction: - Looping through a **string** processes one
character at a time. - Looping through a **list** processes one list
item at a time. - `.strip()` is a string method; it cannot be applied
directly to a list.

## Final Challenge

Starting text:

``` python
report = "  Python, SQL, Git, Python  "
```

Completed tasks: 1. Removed outside spaces. 2. Counted `"Python"`
occurrences → `2`. 3. Split the cleaned string at commas. 4. Looped
through the items and stripped each item. 5. Checked whether the cleaned
text starts with `"Python"` → `True`.

## Errors Corrected

-   `spilt()` vs `split()`.
-   `Pyhton` vs `Python`.
-   Missing quotation marks around text.
-   Case-sensitive variable names.
-   Confusing a whole list with one string item.
-   Using `.strip()` when `.split()` was needed.
-   Looping over a string when the intention was to loop over a list.

## Retention Focus

Day 13 should begin with 2--3 short recall tasks from Day 12. Continue
recycling `.strip()`, `.split()`, and correct loop-target selection in
future exercises.
