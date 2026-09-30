SQL — DAY 1 | 30 SEP 2026

Topic: SQL Basics, SELECT, WHERE, Comparison Operators, AND, OR

==================================================
1. WHAT IS SQL?
==================================================

SQL stands for Structured Query Language.

SQL is used to communicate with relational databases.

It can be used to:
- View data
- Filter data
- Search for specific records
- Select specific columns
- Later: add, update, delete, join, group, and analyze data

For Day 1, the focus was reading and filtering existing data.


==================================================
2. BASIC SELECT
==================================================

SELECT can return values directly.

Examples:

SELECT 10;

SELECT 25;

SELECT 10 + 5;

SELECT 'Hello';

SELECT 'My SQL journey';

SELECT is one of the most important SQL commands.


==================================================
3. VIEW AVAILABLE DATABASES
==================================================

Command:

SHOW DATABASES;

This displays the databases available on the MySQL server.

In our environment, databases included:

information_schema
mysql
performance_schema
sakila
sys
world


==================================================
4. SELECT A DATABASE
==================================================

Command:

USE world;

This tells MySQL that we want to work with the
world database.

Mental model:

USE database_name;


==================================================
5. VIEW TABLES
==================================================

After selecting the world database:

SHOW TABLES;

The world database contains tables including:

city
country
countrylanguage


==================================================
6. DISPLAY DATA FROM A TABLE
==================================================

Example:

SELECT *
FROM City;

The * means:

"Select all columns."

Because a table may contain many rows, LIMIT can
be used.

Example:

SELECT *
FROM City
LIMIT 5;

Meaning:

Display all columns from City, but return only
the first 5 rows.


==================================================
7. LIMIT
==================================================

LIMIT controls how many rows are returned.

Example:

SELECT *
FROM City
LIMIT 3;

This returns only 3 rows.

WHEN WOULD I USE THIS?

When I only need to preview a small amount of data
instead of displaying the entire table.


==================================================
8. SELECT SPECIFIC COLUMNS
==================================================

We do not always need every column.

Example:

SELECT Name
FROM City
LIMIT 5;

This displays only the Name column.

Multiple columns:

SELECT Name, Population
FROM City
LIMIT 5;

Another example:

SELECT Name, District
FROM City
LIMIT 3;

KEY LESSON:

SELECT determines WHAT information I want.


==================================================
9. BASIC QUERY STRUCTURE
==================================================

A useful mental model:

SELECT -> What information do I want?

FROM   -> Which table contains it?

WHERE  -> Which records do I want?

LIMIT  -> How many records should be returned?


Example:

SELECT Name, Population
FROM City
WHERE Population > 1000000
LIMIT 5;


==================================================
10. WHERE
==================================================

WHERE filters rows.

Example:

SELECT Name, District
FROM City
WHERE District = 'Kabol';

Meaning:

Show Name and District only where District is Kabol.

Result included:

Kabul | Kabol


==================================================
11. TEXT VALUES AND QUOTES
==================================================

Text values are written inside quotes.

Example:

WHERE District = 'Kabol'

The exact text matters.

During practice:

'Kabul'

returned 0 rows because the database value was:

'Kabol'

KEY LESSON:

A valid SQL query can return 0 rows if no data
matches the condition.

0 rows does not automatically mean the SQL syntax
is wrong.


==================================================
12. COMPARISON OPERATORS
==================================================

We practiced:

=   Equal to

!=  Not equal to

>   Greater than

<   Less than

>=  Greater than or equal to

<=  Less than or equal to


==================================================
13. EQUAL TO =
==================================================

Example:

SELECT Name, District
FROM City
WHERE District = 'Kabol';

Meaning:

Return rows where District equals Kabol.


==================================================
14. GREATER THAN >
==================================================

Example:

SELECT Name, Population
FROM City
WHERE Population > 1000000;

Meaning:

Return cities with population greater than
1,000,000.


==================================================
15. LESS THAN <
==================================================

Example:

SELECT Name, Population
FROM City
WHERE Population < 500000
LIMIT 5;

Meaning:

Return cities with population below 500,000.


==================================================
16. GREATER THAN OR EQUAL TO >=
==================================================

Example:

SELECT Name, Population
FROM City
WHERE Population >= 1000000
LIMIT 5;

Meaning:

Population can be exactly 1,000,000 OR greater.


==================================================
17. LESS THAN OR EQUAL TO <=
==================================================

Example:

SELECT Name, Population
FROM City
WHERE Population <= 200000
LIMIT 5;

Meaning:

Population can be exactly 200,000 OR lower.


==================================================
18. NOT EQUAL TO !=
==================================================

Example:

SELECT Name, District
FROM City
WHERE District != 'Kabol'
LIMIT 5;

Meaning:

Return records where District is anything except
Kabol.

Mental model:

!= -> "Everything except this value."


==================================================
19. AND
==================================================

AND combines conditions.

With AND, BOTH conditions must be true.

Example:

SELECT Name, Population
FROM City
WHERE Population > 500000
AND Population < 1000000
LIMIT 5;

Meaning:

Population must be:

greater than 500,000

AND

less than 1,000,000.

A row must satisfy BOTH conditions.


==================================================
20. AND WITH INCLUSIVE BOUNDARIES
==================================================

Example:

SELECT Name, Population
FROM City
WHERE Population >= 200000
AND Population <= 300000
LIMIT 5;

Meaning:

Population must be between 200,000 and 300,000,
including the boundary values.


==================================================
21. OR
==================================================

OR means at least ONE condition must be true.

Example:

SELECT Name, District
FROM City
WHERE District = 'Kabol'
OR District = 'Herat';

This returned records matching either district.

KEY DIFFERENCE:

AND -> BOTH conditions must be true.

OR  -> AT LEAST ONE condition must be true.


==================================================
22. FINAL DAY 1 CHALLENGE
==================================================

Situation:

Find cities where population is:

- Greater than or equal to 500,000
- AND less than or equal to 1,000,000

Display:

- Name
- District
- Population

Show:

- First 5 results


Query:

SELECT Name, District, Population
FROM City
WHERE Population >= 500000
AND Population <= 1000000
LIMIT 5;


Result:

Amsterdam | Noord-Holland | 731200
Rotterdam | Zuid-Holland  | 593321
Oran      | Oran          | 609823
Dubai     | Dubai         | 669181
Rosario   | Santa Fé      | 907718


==================================================
23. WHEN WOULD I USE THESE?
==================================================

Situation:
"I want every column from a table."

Use:

SELECT *


Situation:
"I only need employee names and salaries."

Use:

SELECT specific columns


Situation:
"I only want records matching a condition."

Use:

WHERE


Situation:
"I only want the first few results."

Use:

LIMIT


Situation:
"I need values above a number."

Use:

>


Situation:
"I need values below a number."

Use:

<


Situation:
"I need the boundary value included."

Use:

>= or <=


Situation:
"I want everything except one value."

Use:

!=


Situation:
"Two requirements must both be satisfied."

Use:

AND


Situation:
"Either of two conditions can be satisfied."

Use:

OR


==================================================
24. ERRORS AND LESSONS FROM DAY 1
==================================================

1. SQL spelling matters.

During practice:

Pupulation

was typed instead of:

Population

The column name must be spelled correctly.


2. Exact data values matter.

We searched for:

Kabul

but the District value was:

Kabol

The SQL query was valid, but it returned 0 rows.


3. 0 rows is different from an SQL error.

0 rows means:

The query executed, but no records matched.


4. Read error messages carefully.

A misspelled column can cause an error such as:

Unknown column


5. SQL keywords are commonly written in uppercase
for readability.

Example:

SELECT Name
FROM City
WHERE Population > 1000000;

SQL keywords do not have to be uppercase in these
queries, but uppercase makes the query easier to read.


==================================================
25. DAY 1 QUICK REFERENCE
==================================================

Show databases:

SHOW DATABASES;


Choose database:

USE world;


Show tables:

SHOW TABLES;


All columns:

SELECT *
FROM City;


Specific column:

SELECT Name
FROM City;


Multiple columns:

SELECT Name, Population
FROM City;


Limit results:

LIMIT 5;


Filter:

WHERE condition;


Equal:

=


Not equal:

!=


Greater than:

>


Less than:

<


Greater than or equal:

>=


Less than or equal:

<=


Both conditions:

AND


Either condition:

OR


==================================================
26. BASIC QUERY PATTERN
==================================================

SELECT column1, column2
FROM table_name
WHERE condition
LIMIT number;


With multiple conditions:

SELECT column1, column2
FROM table_name
WHERE condition1
AND condition2
LIMIT number;


==================================================
27. KEY LESSONS FROM SQL DAY 1
==================================================

1. SELECT chooses what information to display.

2. FROM chooses the table.

3. WHERE filters records.

4. LIMIT controls how many rows are returned.

5. * means all columns.

6. Multiple columns are separated by commas.

7. Text values need quotes.

8. Comparison operators allow numeric and text
filtering.

9. AND requires both conditions to be true.

10. OR requires at least one condition to be true.

11. A query returning 0 rows is not necessarily
incorrect.

12. Column names and data values must be typed
accurately.

13. Build SQL by thinking:

What information?
-> SELECT

From where?
-> FROM

Which records?
-> WHERE

How many?
-> LIMIT


==================================================
28. ENVIRONMENT PROGRESS
==================================================

MySQL environment is now available across the
three PCs used for this learning journey.

The third-PC setup was environment preparation,
not a separate SQL learning day.

SQL Day 1 continued from the same learning position
after setup.


==================================================
SQL DAY 1 STATUS
==================================================

Learning exercises: Completed

WHERE practice: Completed

Comparison operators:
=, !=, >, <, >=, <= — Completed

AND: Completed

OR: Completed

Final independent challenge: Completed

Day_01_Practice.sql:
Complete script successfully executed with no errors

Topic:
SQL Basics, SELECT, WHERE, Comparison Operators,
AND and OR
