# Python — Day 4: September 15
# Topic: while loops

# Exercise 1: Basic while loop

count = 1

while count <= 5:
    print(count)
    count = count + 1


# Exercise 2: Print "Python" 5 times

count = 1

while count <= 5:
    print("Python")
    count = count + 1


# Exercise 3: Print "Hello" a user-specified number of times

times = input("How many times? ")
times = int(times)

count = 1

while count <= times:
    print("Hello")
    count = count + 1


# Exercise 4: Print numbers from 1 up to a user-specified number

number = input("Till which number? ")
number = int(number)

count = 1

while count <= number:
    print(count)
    count = count + 1
