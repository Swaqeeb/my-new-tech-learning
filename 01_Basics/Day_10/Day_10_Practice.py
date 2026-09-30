# Python — Day 10 | 30 Sep 2026
# Topic: Sets

# ==========================================
# 1. Creating a Set
# ==========================================

numbers = {10, 20, 30}
print("Numbers:", numbers)


# ==========================================
# 2. Sets Keep Unique Values
# ==========================================

numbers = {10, 20, 20, 30, 30, 30}
print("Unique numbers:", numbers)

fruits = {"apple", "banana", "apple", "mango", "banana"}
print("Unique fruits:", fruits)


# ==========================================
# 3. Adding Items
# ==========================================

fruits.add("orange")
print("After adding orange:", fruits)

# Adding an existing value does not create a duplicate
fruits.add("apple")
print("After adding apple again:", fruits)


# ==========================================
# 4. Removing Items
# ==========================================

fruits.remove("banana")
print("After removing banana:", fruits)

# discard() does not give an error if the item does not exist
fruits.discard("banana")
print("After discarding missing banana:", fruits)


# ==========================================
# 5. Membership Check
# ==========================================

if "apple" in fruits:
    print("Apple exists")


# ==========================================
# 6. Length of a Set
# ==========================================

print("Number of fruits:", len(fruits))


# ==========================================
# 7. Loop Through a Set
# ==========================================

print("Fruits:")
for fruit in fruits:
    print(fruit)


# ==========================================
# 8. Set Operations
# ==========================================

team_a = {"Python", "SQL", "Excel"}
team_b = {"Python", "SQL", "Power BI"}

# Intersection — common items
print("Intersection:", team_a & team_b)

# Union — all unique items
print("Union:", team_a | team_b)

# Difference — items in Team A but not Team B
print("Team A only:", team_a - team_b)

# Difference — items in Team B but not Team A
print("Team B only:", team_b - team_a)

# Symmetric difference — items that are not shared
print("Different skills:", team_a ^ team_b)


# ==========================================
# 9. Empty Set
# ==========================================

empty_dictionary = {}
empty_set = set()

print("Type of {}:", type(empty_dictionary))
print("Type of set():", type(empty_set))


# ==========================================
# 10. Build a Set Gradually
# ==========================================

skills = set()

skills.add("Python")
skills.add("SQL")
skills.add("Python")

print("Skills:", skills)


# ==========================================
# 11. Convert a List to a Set
# ==========================================

names = ["Anik", "Tarin", "Anik", "Swaqeeb", "Tarin"]
unique_names = set(names)

print("Unique names:", unique_names)


# ==========================================
# 12. Remove Duplicate Numbers
# ==========================================

number_list = [10, 20, 10, 30, 20, 40, 40, 50]
unique_numbers = set(number_list)

print("Unique numbers from list:", unique_numbers)


# ==========================================
# 13. Real-World PC Application Example
# ==========================================

office_apps = {"Outlook", "Teams", "Excel", "Chrome"}
home_apps = {"Chrome", "Excel", "VS Code", "MySQL"}

print("Apps on both PCs:", office_apps & home_apps)
print("All unique apps:", office_apps | home_apps)
print("Home PC only:", home_apps - office_apps)
print("Different apps:", office_apps ^ home_apps)


# ==========================================
# 14. Final Day 10 Challenge
# ==========================================

system_a = {101, 102, 103, 104, 105}
system_b = {103, 104, 105, 106, 107}

print("Common IDs:", system_a & system_b)
print("All unique IDs:", system_a | system_b)
print("System A only:", system_a - system_b)
print("IDs in only one system:", system_a ^ system_b)


# ==========================================
# Day 10 Quick Reference
# ==========================================

# set()       -> create an empty set
# .add()      -> add an item
# .remove()   -> remove an item; error if missing
# .discard()  -> remove an item safely if it exists
# len()       -> count unique items
# in          -> check whether an item exists
#
# & -> intersection: common items
# | -> union: all unique items
# - -> difference: first set only
# ^ -> symmetric difference: items unique to either side
#
# Sets:
# - store unique values
# - do not support positional indexing
# - should not be relied on for item order