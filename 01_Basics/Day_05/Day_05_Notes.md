Python — Day 5
Date: September 19, 2026
Status: COMPLETED
Goal
Learn how to use Python for loops and range() for repetition, counting, calculations, and user-input-based programs.

1. Basic for Loop
A for loop repeats code for a sequence of values.
for i in range(5):
    print(i)

Output:
0
1
2
3
4

Important Rule
range(5) starts at 0 and stops before 5.

2. Using range(start, stop)
for i in range(1, 6):
    print(i)

Output:
1
2
3
4
5

Important Rule
range(start, stop):
Includes the starting value.
Does NOT include the stopping value.
Therefore:
range(1, 6)

produces:
1, 2, 3, 4, 5


3. Printing Text with the Loop Variable
for i in range(1, 6):
    print("Number:", i)

Output:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

The variable i automatically changes during each iteration.

4. Using range(start, stop, step)
The third value in range() controls how much Python moves each time.
for i in range(2, 11, 2):
    print(i)

Output:
2
4
6
8
10

The format is:
range(start, stop, step)

Example:
range(5, 26, 5)

produces:
5, 10, 15, 20, 25


5. Counting Backward
A negative step can be used to count backward.
for i in range(5, 0, -1):
    print(i)

Output:
5
4
3
2
1

Another example:
for i in range(10, 1, -2):
    print(i)

Output:
10
8
6
4
2

The stop value is still excluded when counting backward.

6. Combining input() with a for Loop
number = input("Enter a number: ")
number = int(number)

for i in range(1, number + 1):
    print(i)

If the user enters 5, the output is:
1
2
3
4
5

We use:
number + 1

because the stop value of range() is not included.

7. Repeating Text
times = input("How many times? ")
times = int(times)

for i in range(1, times + 1):
    print("Hello")

If the user enters 3:
Hello
Hello
Hello

The range() controls how many times the loop runs.
The print() statement controls what is displayed.

8. Printing Text and Numbers Together
for i in range(1, 5):
    print("Hello", i)

Output:
Hello 1
Hello 2
Hello 3
Hello 4

Multiple items inside print() can be separated using commas.

9. Multiplication Table
number = input("Enter a number: ")
number = int(number)

for i in range(1, 11):
    print(number, "X", i, "=", number * i)

If the user enters 5:
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50

Important distinction:
"X"

is text to display, while:
*

is the multiplication operator.

10. Accumulating a Total
A variable can store a running total during a loop.
total = 0

for i in range(1, 6):
    total = total + i

print(total)

Output:
15

The calculation happens like this:
0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15

Important Rule
Initialize:
total = 0

before the loop.
If it is placed inside the loop, it will reset to zero during every iteration.

11. Printing Inside vs Outside a Loop
Inside:
for i in range(1, 6):
    total = total + i
    print(total)

This prints every intermediate total.
Outside:
for i in range(1, 6):
    total = total + i

print(total)

This prints only the final total.
Indentation determines whether a statement belongs to the loop.

12. Dynamic Sum Using User Input
number = input("Add numbers up to: ")
number = int(number)

total = 0

for i in range(1, number + 1):
    total = total + i

print(total)

If the user enters 10:
55

because:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55


13. Sum of Even Numbers
total = 0

for i in range(2, 21, 2):
    total = total + i

print(total)

Output:
110


14. Sum of Odd Numbers
total = 0

for i in range(1, 16, 2):
    total = total + i

print(total)

Output:
64


15. Important Errors and Lessons
Spelling Error
Incorrect:
ramge(1, 6)

Correct:
range(1, 6)

Python produced a NameError because ramge was not defined.
Missing Colon
Incorrect:
for i in range(1, 11)

Correct:
for i in range(1, 11):

A for statement requires :.
Strings vs Integers
input() returns a string.
number = input("Enter a number: ")

Convert it before mathematical calculations:
number = int(number)

Otherwise:
"4" * 3

produces:
444

instead of:
12

Text Needs Quotation Marks
"x"

is text.
Without quotation marks:
x

Python treats it as a variable.
Assignment vs Function Call
Incorrect:
total(total + i)

Correct:
total = total + i

The incorrect version tries to call total like a function.

Key Lessons from Day 5
for loops repeat code automatically.
range(stop) normally starts at 0.
range(start, stop) includes start but excludes stop.
range(start, stop, step) controls the amount of movement.
Negative steps allow backward counting.
The loop variable such as i changes automatically.
input() returns a string.
Use int() when numerical input is required.
Variables can accumulate values inside loops.
Initialize an accumulator before the loop.
Indentation determines what executes inside the loop.
Python error messages often contain useful hints.
Variables remain in memory when working in the interactive Python shell.

Day 5 Status
Python — Day 5: September 19, 2026 — COMPLETED
Main topic: For Loops and range()
Successfully completed practical exercises involving:
Forward counting
Backward counting
Step values
User input
Repeated text
Multiplication tables
Running totals
Even-number sums
Odd-number sums
Debugging common Python errors

