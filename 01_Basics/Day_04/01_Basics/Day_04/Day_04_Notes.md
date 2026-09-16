Complete Day_04_Notes.md
# Python — Day 4: September 15

## Topic: While Loops

## Learning Objectives

Today I learned:

- What loops are
- Why loops are useful
- The `while` loop
- Loop conditions
- Counters
- Increasing a counter
- Using `input()` with a loop
- Using `int()` with user input
- Infinite loops
- Basic loop error troubleshooting

---

## 1. What Is a Loop?

A loop allows Python to repeat a block of code multiple times.

Instead of writing:

```python
print("Python")
print("Python")
print("Python")
print("Python")
print("Python")

we can use a loop to repeat the same action.

2. The while Loop

A while loop repeats code as long as its condition is True.

Basic structure:

while condition:
    # code to repeat

Example:

count = 1

while count <= 5:
    print(count)
    count = count + 1

Output:

1
2
3
4
5
How it works

First:

count = 1

Python checks:

count <= 5

Since 1 <= 5 is True, Python prints 1.

Then:

count = count + 1

changes count from 1 to 2.

Python checks the condition again and continues until count becomes 6.

At that point:

6 <= 5

is False, so the loop stops.

3. Printing Text Repeatedly

We can use a while loop to print text several times.

count = 1

while count <= 5:
    print("Python")
    count = count + 1

Output:

Python
Python
Python
Python
Python
Important: Text vs Variable

This:

print("Python")

prints the text Python.

But this:

print(python)

tells Python to look for a variable named python.

If that variable does not exist, Python gives:

NameError

Therefore, text normally needs quotation marks.

4. The Counter

A counter is a variable used to control how many times a loop runs.

Example:

count = 1

The counter is increased with:

count = count + 1

So the values become:

1
2
3
4
5

The counter helps the loop eventually stop.

5. Why count = count + 1 Is Important

Consider:

count = 1

while count <= 5:
    print(count)

There is no change to count.

Therefore count always remains 1.

The condition:

count <= 5

always remains:

1 <= 5

which is True.

This creates an infinite loop.

6. Infinite Loops

An infinite loop is a loop that does not stop.

Example:

count = 1

while count <= 5:
    print("Python")

Because count never changes, the loop continues forever.

Stopping an Accidental Infinite Loop

In the Python interactive shell, press:

Ctrl + C

to interrupt the loop.

7. User-Controlled Loops

We can ask the user how many times something should be printed.

Example:

times = input("How many times? ")
times = int(times)

count = 1

while count <= times:
    print("Hello")
    count = count + 1

If the user enters:

3

the output is:

Hello
Hello
Hello
Important

input() returns a string.

Therefore:

times = input("How many times? ")

gives us text.

We use:

times = int(times)

to convert that text into an integer.

8. Printing Numbers Up to a User's Number

We can also ask the user for a number and print all numbers from 1 up to that number.

Example:

number = input("Till which number? ")
number = int(number)

count = 1

while count <= number:
    print(count)
    count = count + 1

If the user enters:

4

the output is:

1
2
3
4
9. Errors I Encountered
Error 1: NameError

I initially used:

print(python)

instead of:

print("Python")

Python interpreted python as a variable and could not find that variable.

Lesson

Use quotation marks when printing text:

print("Python")
Error 2: count Was Not Defined

I tried to run:

while count <= times:

before defining count.

Python produced a NameError.

The solution was:

count = 1

before starting the loop.

Lesson

A variable must be defined before using it.

Error 3: Variable Names Must Match

I used:

times

in one place and:

time

in another.

These are different variable names.

Python is case-sensitive and variable names must match exactly.

10. Python Interactive Shell

In the Python shell:

>>>

is the main prompt.

When writing a multi-line block such as a while loop, Python automatically shows:

...

The ... is Python's continuation prompt.

I should not type >>> or ... myself.

After finishing a multi-line block, press Enter twice.

11. Practice Completed
Exercise 1 — Basic Counting Loop
count = 1

while count <= 5:
    print(count)
    count = count + 1

Result:

1
2
3
4
5

Status: Completed

Exercise 2 — Print Python 5 Times
count = 1

while count <= 5:
    print("Python")
    count = count + 1

Status: Completed

Exercise 3 — Print Hello a Specific Number of Times
times = input("How many times? ")
times = int(times)

count = 1

while count <= times:
    print("Hello")
    count = count + 1

Tested successfully with:

3

Result:

Hello
Hello
Hello

Status: Completed

Exercise 4 — Print Numbers Up to a Specific Number
number = input("Till which number? ")
number = int(number)

count = 1

while count <= number:
    print(count)
    count = count + 1

Tested successfully with:

4

Result:

1
2
3
4

Status: Completed

12. Key Takeaways
A loop repeats code.
A while loop runs while its condition is True.
A counter helps control the loop.
count = count + 1 increases the counter.
The counter must eventually make the condition False.
Forgetting to update the counter can create an infinite loop.
input() returns a string.
int() converts a string containing a whole number into an integer.
Variables must be defined before they are used.
Variable names must match exactly.
Text should normally be written inside quotation marks.
Ctrl + C can stop an accidental infinite loop in the Python shell.
Day 4 Status

Python — Day 4: September 15 — COMPLETED

Next lesson:

Python — Day 5


### Now do this on GitHub

Create/open:

```text
01_Basics/Day_04/Day_04_Notes.md
