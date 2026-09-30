PYTHON — DAY 10 | 30 SEP 2026

Topic: Sets

==================================================
1. WHAT IS A SET?
==================================================

A set is a Python collection that stores unique values.

Example:

numbers = {10, 20, 30}

Important characteristics:

- Sets store unique values.
- Duplicate values are automatically removed.
- Set order should not be relied upon.
- Sets do not support positional indexing.
- Sets are useful when uniqueness or comparison between collections matters.


==================================================
2. CREATING A SET
==================================================

Example:

numbers = {10, 20, 30}

print(numbers)

Possible output:

{10, 20, 30}


==================================================
3. DUPLICATE VALUES
==================================================

Example:

numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

Output:

{10, 20, 30}

Even though some numbers were entered multiple times,
the set keeps only one copy of each value.

KEY LESSON:

Set = unique values


==================================================
4. SET ORDER
==================================================

Example:

fruits = {"apple", "banana", "apple", "mango", "banana"}

The output may appear as:

{'mango', 'apple', 'banana'}

or in another order.

Do not rely on the display order of a set.


==================================================
5. ADDING AN ITEM — add()
==================================================

Use add() to add an item to a set.

Example:

fruits.add("orange")

If the value already exists:

fruits.add("apple")

Python does not create another "apple".

KEY LESSON:

List -> append()
Set  -> add()


==================================================
6. REMOVING AN ITEM — remove()
==================================================

Example:

fruits.remove("banana")

This removes "banana".

However, if "banana" does not exist:

fruits.remove("banana")

Python raises:

KeyError

KEY LESSON:

remove() expects the item to exist.


==================================================
7. SAFE REMOVAL — discard()
==================================================

Example:

fruits.discard("banana")

If "banana" exists, it is removed.

If it does not exist, Python does nothing and does
not raise an error.

SITUATION GUIDE:

remove()
-> Remove an item when I expect it to exist.
-> Missing item causes KeyError.

discard()
-> Remove an item if it exists.
-> Missing item causes no error.


==================================================
8. CHECKING MEMBERSHIP — in
==================================================

Example:

if "apple" in fruits:
    print("Apple exists")

Use in when the question is:

"Does this value exist in the set?"


==================================================
9. COUNTING ITEMS — len()
==================================================

Example:

print(len(fruits))

len() returns the number of unique items in the set.

len() also works with collections learned previously:

len(list)
len(tuple)
len(dictionary)
len(set)


==================================================
10. LOOPING THROUGH A SET
==================================================

Example:

for fruit in fruits:
    print(fruit)

A for loop can process every value in a set.

The order should not be relied upon.


==================================================
11. SET INTERSECTION — &
==================================================

Example:

team_a = {"Python", "SQL", "Excel"}
team_b = {"Python", "SQL", "Power BI"}

print(team_a & team_b)

Result:

{'Python', 'SQL'}

INTERSECTION means:

"What do both sets have in common?"

Symbol:

&


==================================================
12. SET UNION — |
==================================================

Example:

print(team_a | team_b)

Result contains:

Python
SQL
Excel
Power BI

UNION means:

"What are all unique items across both sets?"

Symbol:

|


==================================================
13. SET DIFFERENCE — -
==================================================

Example:

print(team_a - team_b)

Result:

{'Excel'}

Meaning:

Items in Team A that are NOT in Team B.

Reverse direction:

print(team_b - team_a)

Result:

{'Power BI'}

IMPORTANT:

Difference is directional.

A - B
-> Items in A but not B

B - A
-> Items in B but not A


==================================================
14. SYMMETRIC DIFFERENCE — ^
==================================================

Example:

print(team_a ^ team_b)

Result:

{'Excel', 'Power BI'}

SYMMETRIC DIFFERENCE means:

"Which items belong to only one of the two sets?"

It removes the values shared by both sets.

Symbol:

^


==================================================
15. SET OPERATION QUICK GUIDE
==================================================

&  -> Intersection
      Common items

|  -> Union
      All unique items

-  -> Difference
      Items in the first set but not the second

^  -> Symmetric Difference
      Items unique to either side


==================================================
16. EMPTY SET
==================================================

Important Python rule:

empty = {}

does NOT create an empty set.

It creates an empty dictionary.

Example:

a = {}
print(type(a))

Result:

<class 'dict'>

To create an empty set:

b = set()

print(type(b))

Result:

<class 'set'>

KEY LESSON:

{}      -> empty dictionary
set()   -> empty set


==================================================
17. BUILDING A SET GRADUALLY
==================================================

Example:

skills = set()

skills.add("Python")
skills.add("SQL")
skills.add("Python")

Result contains:

Python
SQL

The second "Python" does not create a duplicate.


==================================================
18. CONVERTING A LIST TO A SET
==================================================

A set can be used to remove duplicate values from
a list.

Example:

names = ["Anik", "Tarin", "Anik", "Swaqeeb", "Tarin"]

unique_names = set(names)

print(unique_names)

The result contains only:

Anik
Tarin
Swaqeeb

Each name appears once.


==================================================
19. REMOVING DUPLICATE NUMBERS
==================================================

Example:

number_list = [10, 20, 10, 30, 20, 40, 40, 50]

unique_numbers = set(number_list)

The result contains:

10
20
30
40
50

Situation:

"I have duplicate data and only want unique values."

Tool:

set()


==================================================
20. SETS DO NOT SUPPORT INDEXING
==================================================

A list supports positional indexing:

numbers = [10, 20, 30]

numbers[0]

Result:

10

A set does not support positional indexing.

Example:

unique_numbers[0]

Python raises:

TypeError: 'set' object is not subscriptable

WHY?

A set does not provide positional indexing, so there
is no meaningful item at position [0].


==================================================
21. REAL-WORLD EXAMPLE — APPLICATIONS ON TWO PCs
==================================================

office_apps = {"Outlook", "Teams", "Excel", "Chrome"}

home_apps = {"Chrome", "Excel", "VS Code", "MySQL"}

Applications on BOTH PCs:

office_apps & home_apps

Result:

Chrome
Excel


All unique applications:

office_apps | home_apps


Applications on HOME PC only:

home_apps - office_apps

Result:

VS Code
MySQL


Applications that exist on only one of the PCs:

office_apps ^ home_apps

Result contains:

Outlook
Teams
VS Code
MySQL


==================================================
22. FINAL DAY 10 CHALLENGE
==================================================

System A:

system_a = {101, 102, 103, 104, 105}

System B:

system_b = {103, 104, 105, 106, 107}


IDs in both systems:

system_a & system_b

Result:

{103, 104, 105}


All unique IDs:

system_a | system_b

Result:

{101, 102, 103, 104, 105, 106, 107}


System A only:

system_a - system_b

Result:

{101, 102}


IDs existing in only one system:

system_a ^ system_b

Result:

{101, 102, 106, 107}


==================================================
23. CHOOSING THE RIGHT COLLECTION
==================================================

LIST

Use when:
- Order/sequence matters
- Values may change
- Duplicates are allowed

Example:

shopping = ["Rice", "Milk", "Milk"]


TUPLE

Use when:
- Values belong together
- The collection should remain fixed
- Positional access may be useful

Example:

coordinates = (23.8, 90.4)


DICTIONARY

Use when:
- Information naturally has labels and values
- I want to retrieve data using meaningful keys

Example:

employee = {
    "name": "Swaqeeb",
    "department": "IT",
    "salary": 55000
}


SET

Use when:
- Values should be unique
- Duplicates should be eliminated
- I do not need positional indexing
- I want to compare groups of values

Example:

employee_ids = {101, 102, 103}


==================================================
24. WHEN WOULD I USE THIS?
==================================================

Situation:
"I only want unique employee IDs."

Use:
SET


Situation:
"I want to remove duplicate values from a list."

Use:
set(list_name)


Situation:
"I want to know what two groups have in common."

Use:
INTERSECTION (&)


Situation:
"I want every unique value from two groups."

Use:
UNION (|)


Situation:
"I want values in Group A but not Group B."

Use:
DIFFERENCE (-)


Situation:
"I want values that appear on only one side."

Use:
SYMMETRIC DIFFERENCE (^)


Situation:
"I want to remove a set item, but I do not know
whether it exists."

Use:
discard()


Situation:
"I want to check whether a value exists."

Use:
in


==================================================
25. ERRORS AND LESSONS FROM DAY 10
==================================================

1. Variable spelling matters.

Example:

numbers

and

nunbers

are different variable names.

A spelling mistake caused:

NameError


2. Sets do not support indexing.

Trying:

unique_numbers[0]

caused:

TypeError: 'set' object is not subscriptable


3. remove() can raise KeyError when the item does
not exist.

discard() can be used when safe removal is needed.


4. Difference is directional.

A - B

is different from:

B - A


5. Union and symmetric difference are different.

Union:
All unique values from both sets.

Symmetric difference:
Values that occur on only one side.


6. Python strings are case-sensitive.

"Outlook"

and

"outlook"

are different values.


==================================================
26. DAY 10 QUICK REFERENCE
==================================================

Create set:

numbers = {10, 20, 30}


Empty set:

numbers = set()


Add:

numbers.add(40)


Remove:

numbers.remove(20)


Safe remove:

numbers.discard(20)


Membership:

20 in numbers


Length:

len(numbers)


Loop:

for number in numbers:
    print(number)


Intersection:

a & b


Union:

a | b


Difference:

a - b


Symmetric difference:

a ^ b


Remove duplicates from a list:

unique_values = set(my_list)


==================================================
27. KEY LESSONS FROM DAY 10
==================================================

1. Sets are mainly useful for UNIQUE values.

2. Do not rely on set order.

3. Sets do not support positional indexing.

4. add() adds values.

5. remove() can raise an error for a missing value.

6. discard() safely ignores a missing value.

7. Intersection finds common values.

8. Union combines all unique values.

9. Difference is directional.

10. Symmetric difference finds values unique to
either side.

11. Converting a list to a set is an easy way to
remove duplicates.

12. Choose the collection based on the problem:

List       -> ordered and changeable
Tuple      -> ordered and fixed
Dictionary -> key-value information
Set        -> unique values and group comparison

13. Focus on:

Situation -> Concept -> Syntax

rather than trying to memorize every command.


==================================================
DAY 10 STATUS
==================================================

Learning exercises: Completed
Final challenge: Completed
Day_10_Practice.py: Successfully executed with no errors

Topic:
Sets

