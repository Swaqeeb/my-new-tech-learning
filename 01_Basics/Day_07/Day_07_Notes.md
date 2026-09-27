# Python — Day 07

**Topic:** Lists  
**Status:** Completed  
**Started:** September 21, 2026  
**Completed:** September 27, 2026

## 1. Creating a List

```python
numbers = [10, 20, 30, 40, 50]
```

A list can store multiple values in one variable.

## 2. List Indexing

Python list indexes start at `0`.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[-1])  # 50
```

## 3. Changing a List Item

```python
numbers[2] = 99
```

This changes the value at index `2`.

## 4. Adding Items

`append()` adds an item to the end:

```python
numbers.append(60)
```

`insert()` adds an item at a specific index:

```python
numbers.insert(1, 15)
```

## 5. Removing Items

`remove()` removes a value:

```python
numbers.remove(30)
```

`pop()` removes an item using its index:

```python
numbers.pop(2)
```

## 6. List Length

```python
print(len(numbers))
```

`len()` tells us how many items are in the list.

## 7. Looping Through a List

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

A `for` loop processes each item one at a time.

## 8. Loop with Calculation

```python
for number in numbers:
    print(number * 2)
```

The calculation is performed separately on each list item.

## 9. Accumulator with a List

```python
numbers = [10, 20, 30]
total = 0

for number in numbers:
    total = total + number

print(total)
```

Output:

```text
60
```

## 10. List + for + if + Accumulator

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    if number > 20:
        total = total + number

print(total)
```

Output:

```text
120
```

## 11. Checking a Value with `in`

```python
fruits = ["apple", "banana", "mango"]

if "banana" in fruits:
    print("banana is available")
```

The `in` operator checks whether a value exists in a list.

## 12. List Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[2:])   # [30, 40, 50]
```

**Rule:** The start index is included, but the stop index is excluded.

## 13. Slicing with Step

```python
print(numbers[::2])
```

Output:

```text
[10, 30, 50]
```

A step of `2` means move two indexes at a time.

## 14. Reverse Slicing

```python
print(numbers[::-1])
```

Output:

```text
[50, 40, 30, 20, 10]
```

## 15. Sorting

```python
numbers.sort()
```

Sorts from smallest to largest.

```python
numbers.sort(reverse=True)
```

Sorts from largest to smallest.

## 16. `count()`

```python
numbers = [10, 20, 20, 30, 20, 40]

print(numbers.count(20))
```

Output:

```text
3
```

`count()` tells us how many times a value appears.

## 17. `index()`

```python
numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))
```

Output:

```text
1
```

`index()` returns the index of the first occurrence.

## 18. Useful Built-in Functions

```python
len(numbers)
min(numbers)
max(numbers)
sum(numbers)
```

- `len()` → number of items
- `min()` → smallest value
- `max()` → largest value
- `sum()` → total of all values

## 19. Comparison Operators Practiced

- `>` → greater than
- `>=` → greater than or equal to
- `<` → less than
- `<=` → less than or equal to

## 20. Important Lessons

- Python list indexes start at `0`.
- Negative indexes count from the end.
- Slicing includes the start but excludes the stop.
- A `for` loop processes every item in a list.
- A calculation inside a loop is applied separately to each item.
- An accumulator should normally be initialized before the loop.
- `total = total + number` keeps a running total.
- Interactive Python shell variables keep their values until they are reset.
- `count()` tells how many times a value appears.
- `index()` tells the position of the first occurrence.
- Correct indentation is important inside `for` and `if` blocks.

## Final Day 07 Challenge

```python
numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    if number > 20:
        total = total + number

print(total)
```

Output:

```text
120
```

**Day 07 completed successfully.**
