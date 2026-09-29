# Python — Day 9 Practice
# Date: September 29, 2026
# Topic: Dictionaries


# 1. Create a dictionary
Student = {
    "name": "Swaqeeb",
    "age": 31
}

print(Student)


# 2. Access values
print(Student["name"])
print(Student["age"])


# 3. Change an existing value
Student["age"] = 32
print(Student)


# 4. Add a new key-value pair
Student["city"] = "Dhaka"
print(Student)

Student["city"] = "Dinajpur"
print(Student)


# 5. Remove an item using pop()
Student.pop("city")
print(Student)


# 6. Count key-value pairs
print(len(Student))


# 7. Loop through keys
for key in Student:
    print(key)


# 8. Loop through values
for value in Student.values():
    print(value)


# 9. Loop through keys and values
for key, value in Student.items():
    print(key, value)


# 10. Add another key-value pair
Student["Job"] = "Engineer"
print(Student)

for key, value in Student.items():
    print(key, value)


# 11. Check whether keys exist
if "age" in Student:
    print("Age exists")

if "salary" in Student:
    print("Salary exists")
else:
    print("Salary does not exist")


# 12. Safe access using get()
print(Student.get("age"))
print(Student.get("Salary"))
print(Student.get("Salary", "Not Available"))


# 13. Show keys, values, and items
print(Student.keys())
print(Student.values())
print(Student.items())


# 14. Delete a key-value pair
del Student["Job"]
print(Student)


# 15. Clear a dictionary
Test = {
    "a": 1,
    "b": 2,
    "c": 3
}

Test.clear()

print(Test)
print(len(Test))


# 16. Copy a dictionary
Student_copy = Student.copy()

Student_copy["age"] = 40

print(Student_copy)
print(Student)


# 17. Final independent practice
Employe = {
    "name": "Swaqeeb",
    "department": "IT",
    "salary": 50000
}

print(Employe)


# Change salary
Employe["salary"] = 55000
print(Employe)


# Add city
Employe["city"] = "Dinajpur"
print(Employe)


# Print all keys and values
for key, value in Employe.items():
    print(key, value)


# Safely retrieve a missing key
print(Employe.get("phone", "Not Available"))


# --------------------------------------------------
# Day 9 Quick Reference
# --------------------------------------------------

# dictionary["key"]       -> access a value
# dictionary["key"] = x   -> change or add a value
# dictionary.get("key")   -> safely retrieve a value
# "key" in dictionary     -> check whether a key exists
# dictionary.keys()       -> all keys
# dictionary.values()     -> all values
# dictionary.items()      -> keys and values
# dictionary.pop("key")   -> remove and return a value
# del dictionary["key"]   -> delete a key-value pair
# dictionary.clear()      -> remove everything
# dictionary.copy()       -> make a separate copy
# len(dictionary)         -> number of key-value pairs