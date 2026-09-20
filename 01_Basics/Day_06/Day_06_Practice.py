# Python Day 06 Practice
# Date: September 20, 2026
# Topic: While Loops, Break, Continue, and while True


# 1. Basic while loop
print("1. Basic while loop")

number = 1
while number <= 5:
    print(number)
    number = number + 1


# 2. Count by 2
print("\n2. Count by 2")

number = 2
while number <= 10:
    print(number)
    number = number + 2


# 3. Count backward
print("\n3. Count backward")

number = 5
while number >= 1:
    print(number)
    number = number - 1


# 4. Sum numbers from 1 to 5
print("\n4. Sum 1 to 5")

number = 1
total = 0

while number <= 5:
    total = total + number
    number = number + 1

print("Total:", total)


# 5. Even numbers and their sum
print("\n5. Even numbers from 2 to 10")

number = 2
total = 0

while number <= 10:
    print(number)
    total = total + number
    number = number + 2

print("Total:", total)


# 6. Break
print("\n6. Break at 5")

number = 1

while number <= 10:
    print(number)

    if number == 5:
        break

    number = number + 1


# 7. Continue
print("\n7. Skip 3")

number = 0

while number < 5:
    number = number + 1

    if number == 3:
        continue

    print(number)


# 8. Skip 3 and 7
print("\n8. Skip 3 and 7")

number = 0

while number < 10:
    number = number + 1

    if number == 3 or number == 7:
        continue

    print(number)


# 9. while True with break
print("\n9. while True with break")

number = 1

while True:
    print(number)

    if number == 5:
        break

    number = number + 1


# 10. Final challenge
print("\n10. Final challenge")

number = 0
total = 0

while number < 10:
    number = number + 1

    if number == 3 or number == 7:
        continue

    if number == 9:
        break

    total = total + number

print("Final total:", total)
