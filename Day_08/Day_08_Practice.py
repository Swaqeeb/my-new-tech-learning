# Python — Day 8
# Date: September 28, 2026
# Topic: Tuples


# 1. Create a tuple
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)


# 2. Tuple indexing
print("Index 2:", numbers[2])


# 3. Negative indexing
print("Last item:", numbers[-1])
print("Second last item:", numbers[-2])


# 4. Length of a tuple
fruits = ("apple", "banana", "mango", "orange")
print("Number of fruits:", len(fruits))


# 5. Loop through a tuple
print("\nFruits:")
for fruit in fruits:
    print(fruit)


# 6. Tuple + calculation
numbers2 = (5, 10, 15)

print("\nNumbers multiplied by 2:")
for number in numbers2:
    print(number * 2)


# 7. Check values using in
print("\nIs banana in fruits?")
print("banana" in fruits)

print("Is pineapple in fruits?")
print("pineapple" in fruits)


# 8. count()
numbers3 = (10, 20, 20, 30, 20, 40)
print("\nNumber of times 20 appears:", numbers3.count(20))


# 9. index()
numbers4 = (10, 20, 30, 20, 40)
print("First index of 20:", numbers4.index(20))


# 10. Tuple slicing
numbers5 = (10, 20, 30, 40, 50)

print("\nSlice [1:4]:", numbers5[1:4])
print("Slice [:3]:", numbers5[:3])
print("Slice [2:]:", numbers5[2:])
print("Every second item:", numbers5[::2])
print("Reversed tuple:", numbers5[::-1])


# 11. Single-item tuple
single = (10,)
print("\nSingle-item tuple:", single)


# 12. Tuple unpacking
student = ("Anik", 30, "Python")
name, age, course = student

print("\nStudent name:", name)
print("Student age:", age)
print("Student course:", course)


# 13. Tuple + loop + condition
numbers6 = (10, 20, 30, 40, 50)

print("\nNumbers greater than 25:")
for number in numbers6:
    if number > 25:
        print(number)


# 14. Tuple + condition + accumulator
total = 0

for number in numbers6:
    if number > 25:
        total = total + number

print("Total of numbers greater than 25:", total)


# 15. Convert list to tuple
number_list = [10, 20, 30, 40]
number_tuple = tuple(number_list)

print("\nList converted to tuple:", number_tuple)


# 16. Convert tuple to list
fruit_tuple = ("apple", "banana", "mango")
fruit_list = list(fruit_tuple)

fruit_list.append("orange")

print("Tuple converted to list:", fruit_list)


# 17. Final Day 8 challenge
challenge_numbers = (5, 10, 15, 20, 25, 30, 35, 40)
total = 0

for number in challenge_numbers:
    if number > 15:
        total = total + number

print("\nFinal challenge total:", total)