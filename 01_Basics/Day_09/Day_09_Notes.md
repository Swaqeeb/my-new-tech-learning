# Python — Day 9
Date: September 29, 2026
Status: Completed
Topic: Dictionaries

## 1. What is a Dictionary?

A dictionary stores information as key-value pairs.

Example:

Student = {
    "name": "Swaqeeb",
    "age": 31
}

Here:
"name" is a key
"Swaqeeb" is its value
"age" is a key
31 is its value

Important:
- Colon : connects a key with its value.
- Comma , separates different key-value pairs.
- Dictionary keys are case-sensitive.

---

## 2. Access a Value

Use the key inside square brackets.

Example:

print(Student["name"])
print(Student["age"])

Output:

Swaqeeb
31

---

## 3. Change an Existing Value

Example:

Student["age"] = 32

If the key already exists, Python changes its value.

Pattern:

dictionary["key"] = new_value

---

## 4. Add a New Key-Value Pair

Example:

Student["city"] = "Dinajpur"

If the key does not already exist, Python creates a new key-value pair.

Important:

dictionary["key"] = value

can do two things:

Existing key → changes the value
New key → adds a new key-value pair

---

## 5. Remove an Item with pop()

Example:

Student.pop("city")

.pop() removes the key-value pair and returns the removed value.

Use .pop() when I want to remove something and also get its value back.

---

## 6. Remove an Item with del

Example:

del Student["city"]

Pattern:

del dictionary["key"]

Deleting the key also deletes its associated value.

Use del when I know the key and simply want to delete it.

---

## 7. Remove Everything with clear()

Example:

Test = {"a": 1, "b": 2, "c": 3}

Test.clear()

print(Test)

Output:

{}

{} means the dictionary still exists, but it is empty.

len(Test)

Output:

0

---

## 8. Number of Items with len()

Example:

len(Student)

len() tells me how many key-value pairs are in the dictionary.

---

## 9. Check Whether a Key Exists

Use the in operator.

Example:

if "age" in Student:
    print("Age exists")

Use this when I want to check whether a key exists before doing something with it.

---

## 10. Safe Access with get()

Example:

Student.get("age")

If the key exists, its value is returned.

If the key does not exist:

Student.get("salary")

returns:

None

This avoids a KeyError.

I can also provide a default value:

Student.get("salary", "Not Available")

Output:

Not Available

Pattern:

dictionary.get("key", "default value")

---

## 11. Direct Access vs get()

Direct access:

Student["salary"]

If the key does not exist:

KeyError

Safe access:

Student.get("salary")

If the key does not exist:

None

Therefore, use .get() when I am not sure whether a key exists.

---

## 12. Get All Keys

Example:

Student.keys()

This returns all dictionary keys.

Loop:

for key in Student.keys():
    print(key)

Remember:

.keys() → keys only

---

## 13. Get All Values

Example:

Student.values()

Loop:

for value in Student.values():
    print(value)

Remember:

.values() → values only

---

## 14. Get Keys and Values Together

Example:

Student.items()

Loop:

for key, value in Student.items():
    print(key, value)

Remember:

.items() → keys + values

The key and value are unpacked into two variables.

---

## 15. Dictionary Loop Shortcut

Looping directly through a dictionary gives its keys:

for key in Student:
    print(key)

To get both keys and values:

for key, value in Student.items():
    print(key, value)

---

## 16. Copy a Dictionary

Example:

Student_copy = Student.copy()

The copy can then be changed separately.

Example:

Student_copy["age"] = 40

Changing Student_copy does not change the original Student dictionary.

Use .copy() when I want to experiment with or modify a separate copy while keeping the original data unchanged.

---

## 17. Important Method Pattern

Remember these together:

.keys()    → all keys
.values()  → all values
.items()   → all key-value pairs

All three method names are lowercase and plural.

---

## 18. Common Errors I Practiced Today

### Wrong key/value separator

Wrong:

Student = {"name", "Swaqeeb", "age": 31}

Correct:

Student = {"name": "Swaqeeb", "age": 31}

Use : between a key and value.

---

### Text value without quotation marks

Wrong:

Student["city"] = Dinajpur

Correct:

Student["city"] = "Dinajpur"

Without quotes, Python thinks Dinajpur is a variable.

---

### Wrong method name

Wrong:

Student.value()

Correct:

Student.values()

Wrong:

Student.item()

Correct:

Student.items()

Wrong:

Student.Keys()

Correct:

Student.keys()

Python method names are case-sensitive.

---

### Variable-name spelling

Employe, Employee, Emplyee, and Emloye are different names to Python.

Variable names must be typed consistently.

---

### Typo in a dictionary key

Example:

Employe["slary"] = 55000

does NOT change:

"salary"

Instead, Python creates a new key called:

"slary"

Therefore, dictionary key spelling is important.

---

### Deleting a key that does not exist

Example:

del Employe["slaty"]

If "slaty" does not exist, Python gives:

KeyError

---

## 19. When Would I Use This?

### Dictionary

Use a dictionary when information has meaningful labels.

Example:

Employee = {
    "name": "Swaqeeb",
    "department": "IT",
    "salary": 55000,
    "city": "Dinajpur"
}

This is useful because each value has a meaningful key.

### Situation → Tool

Need one known value
→ dictionary["key"]

Key might not exist
→ .get()

Need to check whether a key exists
→ in

Need to change an existing value
→ dictionary["key"] = new_value

Need to add new information
→ dictionary["new_key"] = value

Need to remove and receive the removed value
→ .pop()

Need to simply delete a known key
→ del

Need to remove everything
→ .clear()

Need all keys
→ .keys()

Need all values
→ .values()

Need both keys and values
→ .items()

Need a separate copy
→ .copy()

Need number of key-value pairs
→ len()

---

## 20. Choosing Between List, Tuple and Dictionary

List:
Use when I need an ordered collection of items that can change.

Tuple:
Use when I need a fixed collection that should normally not change.

Dictionary:
Use when I need labeled key-value relationships.

The goal is not to memorize every command.

Think:

Situation → choose the concept → remember/look up the syntax → use it.

---

## 21. Final Practice

Created an employee dictionary containing:

- name
- department
- salary

Changed salary from 50000 to 55000.

Added a city.

Practiced deleting accidentally created keys.

Looped through keys and values using .items().

Practiced safe access to a missing key using .get() with a default value.

---

## Key Lessons from Day 9

- Dictionaries store key-value pairs.
- Keys give meaningful labels to values.
- Use [] to access or modify values.
- The same assignment syntax can add a new key or update an existing key.
- Use in to check whether a key exists.
- Use .get() for safe retrieval.
- Use .keys(), .values(), and .items() for different kinds of dictionary data.
- Use .pop() or del to remove entries.
- Use .clear() to empty a dictionary.
- Use .copy() to make a separate copy.
- Dictionary keys and Python variable names must be typed accurately.
- Reading Python error messages can help identify and correct mistakes.
- Focus on understanding when to use a concept rather than memorizing every command.

