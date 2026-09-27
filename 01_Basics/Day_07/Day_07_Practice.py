# Python Day 07 Practice
# Topic: Lists

# 1. Creating and printing a list

numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)


# 2. List indexing

print("First item:", numbers[0])
print("Third item:", numbers[2])
print("Last item:", numbers[-1])


# 3. Adding items

numbers.append(60)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)


# 4. Removing items

numbers.remove(30)
print("After remove:", numbers)

removed_item = numbers.pop(2)
print("Popped item:", removed_item)
print("After pop:", numbers)


# 5. List length

print("Number of items:", len(numbers))


# 6. Loop through a list

fruits = ["apple", "banana", "mango"]

print("Fruits:")

for fruit in fruits:
    print(fruit)


# 7. Loop with calculation

practice_numbers = [10, 20, 30, 40, 50]

print("Numbers multiplied by 2:")

for number in practice_numbers:
    print(number * 2)


# 8. Accumulator

total = 0

for number in practice_numbers:
    total = total + number

print("Total:", total)


# 9. List + if + accumulator

total = 0

for number in practice_numbers:
    if number > 20:
        total = total + number

print("Total of numbers greater than 20:", total)


# 10. Check an item with in

if "banana" in fruits:
    print("banana is available")


# 11. List slicing

slice_numbers = [10, 20, 30, 40, 50]

print("Slice 1:4:", slice_numbers[1:4])
print("First three:", slice_numbers[:3])
print("From index 2:", slice_numbers[2:])


# 12. Slicing with step

print("Every second item:", slice_numbers[::2])


# 13. Reverse slicing

print("Reversed:", slice_numbers[::-1])


# 14. Sorting

sort_numbers = [40, 10, 50, 20, 30]

sort_numbers.sort()
print("Ascending:", sort_numbers)

sort_numbers.sort(reverse=True)
print("Descending:", sort_numbers)


# 15. count()

count_numbers = [10, 20, 20, 30, 20, 40]

print("20 appears:", count_numbers.count(20), "times")


# 16. index()

index_numbers = [10, 20, 30, 20, 40]

print("First index of 20:", index_numbers.index(20))


# 17. Useful built-in functions

final_numbers = [10, 30, 20, 50, 40]

print("Length:", len(final_numbers))
print("Minimum:", min(final_numbers))
print("Maximum:", max(final_numbers))
print("Sum:", sum(final_numbers))


# 18. Final Day 07 Challenge

numbers = [10, 20, 30, 40, 50]
total = 0

for number in numbers:
    if number > 20:
        total = total + number

print("Final challenge total:", total)