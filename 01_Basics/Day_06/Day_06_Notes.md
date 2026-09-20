PYTHON — DAY 06 NOTES
Date: September 20, 2026
Status: Completed
Topic: While Loops, Break, Continue, and while True


1. WHILE LOOP

A while loop repeats code as long as a condition is True.

Example:

number = 1

while number <= 5:
    print(number)
    number = number + 1

Output:
1
2
3
4
5


2. COUNTING FORWARD

number = 1

while number <= 10:
    print(number)
    number = number + 1

The number must be updated inside the loop.


3. COUNTING WITH A STEP

Example — even numbers:

number = 2

while number <= 10:
    print(number)
    number = number + 2

Output:
2
4
6
8
10


4. COUNTING BACKWARD

number = 5

while number >= 1:
    print(number)
    number = number - 1

Output:
5
4
3
2
1

For backward counting, the condition often uses >= and the
counter decreases.


5. WHILE LOOP WITH USER INPUT

number = int(input("Enter a number: "))
count = 1

while count <= number:
    print(count)
    count = count + 1

If the user enters 5, the program prints 1 through 5.


6. ACCUMULATION WITH WHILE

total = 0
number = 1

while number <= 5:
    total = total + number
    number = number + 1

print(total)

Output:
15

Important:
Initialize total before the loop.


7. SUM OF EVEN NUMBERS

number = 2
total = 0

while number <= 10:
    total = total + number
    print(number)
    number = number + 2

print(total)

Output:
2
4
6
8
10
30


8. BREAK

break immediately stops a loop.

number = 1

while number <= 20:
    print(number)

    if number == 7:
        break

    number = number + 1

Output:
1
2
3
4
5
6
7


9. CONTINUE

continue skips the rest of the current iteration and starts
the next iteration.

number = 0

while number < 5:
    number = number + 1

    if number == 3:
        continue

    print(number)

Output:
1
2
4
5


10. USING OR

Multiple conditions can be combined using or.

if number == 3 or number == 7:
    continue

This skips both 3 and 7.


11. CONTINUE WITH ACCUMULATION

number = 0
total = 0

while number < 5:
    number = number + 1

    if number == 3:
        continue

    total = total + number

print(total)

Output:
12

The numbers added are:
1 + 2 + 4 + 5 = 12


12. IMPORTANT CONTINUE RULE

With a while loop, be careful where the counter is updated.

A safe pattern is:

number = 0

while number < 10:
    number = number + 1

    if number == 5:
        continue

If the counter update is placed after continue, the program
may become an infinite loop.


13. WHILE TRUE

while True creates a loop whose condition is always True.

Example:

number = 1

while True:
    print(number)

    if number == 5:
        break

    number = number + 1

Output:
1
2
3
4
5

break is used to stop the loop.


14. WHILE TRUE WITH USER INPUT

total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total = total + number

print(total)

The program repeatedly accepts numbers until the user enters 0.


15. FINAL DAY 06 CHALLENGE

Goal:
- Process numbers 1 through 10
- Skip 3 and 7
- Stop when reaching 9
- Add all accepted numbers

number = 0
total = 0

while number < 10:
    number = number + 1

    if number == 3 or number == 7:
        continue

    if number == 9:
        break

    total = total + number

print(total)

Output:
26

Calculation:
1 + 2 + 4 + 5 + 6 + 8 = 26


16. COMMON ERRORS PRACTICED TODAY

1. Missing colon after while or if
2. Incorrect indentation
3. Putting code underneath break
4. Putting another condition underneath continue
5. Forgetting to update a while-loop counter
6. Using the wrong comparison condition
7. Not resetting variables in the interactive Python shell
8. Starting the same loop again after it has already completed


17. KEY LESSONS

- while repeats while its condition is True.
- The loop variable usually needs to change.
- break stops a loop immediately.
- continue skips the current iteration.
- or can combine alternative conditions.
- while True is useful when the stopping condition is handled
  inside the loop with break.
- Indentation controls which statements belong to while and if.
- Code after break in the same block will not execute.
- Be especially careful with counter updates when using continue.
- Reset variables when repeating experiments in the interactive shell.
