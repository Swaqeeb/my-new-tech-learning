# Python — Day 8

**Date:** September 28, 2026  
**Status:** Completed  
**Topic:** Tuples

## 1. What Is a Tuple?

A tuple stores multiple values in one variable.

```python
numbers = (10, 20, 30, 40, 50)
```

Main difference:

- List → changeable (mutable)
- Tuple → not changeable (immutable)

---

## 2. Tuple Indexing

Tuple indexing starts from `0`.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[2])
```

Output:

```text
30
```

---

## 3. Negative Indexing

Negative indexing starts from the end.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[-2])
```

Output:

```text
50
40
```

---

## 4. Tuples Are Immutable

A tuple cannot be changed directly after it is created.

```python
numbers = (10, 20, 30, 40, 50)
numbers[2] = 99
```

This causes:

```text
TypeError: 'tuple' object does not support item assignment
```

A list is mutable, but a tuple is immutable.

---

## 5. len() with a Tuple

`len()` tells us how many items are inside a tuple.

```python
fruits = ("apple", "banana", "mango", "orange")

print(len(fruits))
```

Output:

```text
4
```

---

## 6. Loop Through a Tuple

```python
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
mango
```

---

## 7. Tuple + Calculation

```python
numbers = (5, 10, 15)

for number in numbers:
    print(number * 2)
```

Output:

```text
10
20
30
```

---

## 8. Check an Item with `in`

The `in` operator checks whether a value exists inside a tuple.

```python
fruits = ("apple", "banana", "mango")

print("banana" in fruits)
print("orange" in fruits)
```

Output:

```text
True
False
```

---

## 9. count()

`count()` tells us how many times a value appears.

```python
numbers = (10, 20, 20, 30, 20, 40)

print(numbers.count(20))
```

Output:

```text
3
```

---

## 10. index()

`index()` gives the position of the first occurrence of a value.

```python
numbers = (10, 20, 30, 20, 40)

print(numbers.index(20))
```

Output:

```text
1
```

Remember that Python indexing starts from `0`.

---

## 11. Tuple Slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])
```

Output:

```text
(20, 30, 40)
(10, 20, 30)
(30, 40, 50)
(10, 30, 50)
(50, 40, 30, 20, 10)
```

Remember:

- Start index is included.
- Stop index is excluded.
- `[::-1]` reverses the tuple.

---

## 12. Single-Item Tuple

A single-item tuple requires a comma.

```python
a = (10)
b = (10,)
```

`a` is an integer.

`b` is a tuple.

**The comma makes a single-item tuple.**

---

## 13. Tuple Unpacking

Tuple values can be assigned to separate variables.

```python
student = ("Anik", 30, "Python")

name, age, course = student

print(name)
print(age)
print(course)
```

Output:

```text
Anik
30
Python
```

The number of variables should match the number of values in the tuple.

---

## 14. Tuple + Loop + Condition

```python
numbers = (10, 20, 30, 40, 50)

for number in numbers:
    if number > 25:
        print(number)
```

Output:

```text
30
40
50
```

---

## 15. Tuple + Condition + Accumulator

```python
numbers = (10, 20, 30, 40, 50)
total = 0

for number in numbers:
    if number > 25:
        total = total + number

print(total)
```

Output:

```text
120
```

---

## 16. Convert List to Tuple

```python
numbers = [10, 20, 30, 40]
numbers_tuple = tuple(numbers)

print(numbers_tuple)
```

Output:

```text
(10, 20, 30, 40)
```

---

## 17. Convert Tuple to List

```python
fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)
fruits_list.append("orange")

print(fruits_list)
```

Output:

```text
['apple', 'banana', 'mango', 'orange']
```

---

## 18. Final Day 8 Challenge

```python
numbers = (5, 10, 15, 20, 25, 30, 35, 40)
total = 0

for number in numbers:
    if number > 15:
        total = total + number

print(total)
```

Output:

```text
150
```

Calculation:

```text
20 + 25 + 30 + 35 + 40 = 150
```

---

## Important Lessons from Day 8

1. Tuples use parentheses `()`.
2. Tuples are immutable.
3. Tuple indexing starts from `0`.
4. Negative indexes count from the end.
5. Tuples can be looped through.
6. Tuples support slicing.
7. `count()` counts occurrences.
8. `index()` finds the first matching position.
9. `in` checks whether a value exists.
10. A single-item tuple requires a comma.
11. Tuple values can be unpacked into separate variables.
12. Lists can be converted into tuples.
13. Tuples can be converted into lists.
14. Tuples work with loops, conditions, and accumulators.

---

## Mistakes and Debugging Practiced

- Misspelled variable names such as `numbers` and `numbsers`.
- Used `number` instead of `numbers` in a loop.
- Corrected indentation after an `if` statement.
- Remembered quotation marks around strings.
- Learned that Python variable names are case-sensitive.
- `Print` and `print` are different.
- `Course` and `course` are different variables.
- Corrected `locaiton` to `location`.
- Remembered to reset `total = 0` before rerunning an accumulator.
- Learned that old variables can remain in the interactive Python shell and cause unexpected results.
- Practiced reading Python error messages and correcting the code.

---

## Day 8 Result

**Python Day 8 completed successfully.**

**Date:** September 28, 2026  
**Main Topic:** Tuples  
**Final Challenge Result:** `150`
