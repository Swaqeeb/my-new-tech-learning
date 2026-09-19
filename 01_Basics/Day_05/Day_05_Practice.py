# ============================================
# Python — Day 5 Practice
# Date: September 19, 2026
# Topic: For Loops and range()
# ============================================


# 1. Basic for loop
print("1. Basic for loop")

for i in range(5):
    print(i)


# 2. Counting from 1 to 5
print("\n2. Counting from 1 to 5")

for i in range(1, 6):
    print(i)


# 3. Printing text with a loop variable
print("\n3. Number labels")

for i in range(1, 6):
    print("Number:", i)


# 4. Using a step
print("\n4. Counting by 2")

for i in range(2, 11, 2):
    print(i)


# 5. Counting backward
print("\n5. Counting backward")

for i in range(5, 0, -1):
    print(i)


# 6. Repeat text using user input
print("\n6. Repeat Hello")

times = input("How many times? ")
times = int(times)

for i in range(1, times + 1):
    print("Hello", i)


# 7. Multiplication table
print("\n7. Multiplication Table")

number = input("Enter a number: ")
number = int(number)

for i in range(1, 11):
    print(number, "X", i, "=", number * i)


# 8. Sum numbers up to user input
print("\n8. Sum Numbers")

number = input("Add numbers up to: ")
number = int(number)

total = 0

for i in range(1, number + 1):
    total = total + i

print("Total:", total)


# 9. Sum even numbers from 2 to 20
print("\n9. Sum of Even Numbers")

total = 0

for i in range(2, 21, 2):
    total = total + i

print("Total:", total)


# 10. Sum odd numbers from 1 to 15
print("\n10. Sum of Odd Numbers")

total = 0

for i in range(1, 16, 2):
    total = total + i

print("Total:", total)


# ============================================
# End of Day 5 Practice
# ============================================