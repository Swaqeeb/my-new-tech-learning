# SQL — Day 1

**Started:** 28 September 2026  
**Continued:** 29 September 2026  
**Status:** In Progress

## Topic
Introduction to SQL and Reading Data

## What I Learned

### 1. SELECT
`SELECT` is used to retrieve or display data.

```sql
SELECT 10;
SELECT 25;
```

### 2. Simple Calculations
SQL can perform calculations.

```sql
SELECT 10 + 5;
```

Result: `15`

### 3. Displaying Text
Text values are written inside quotation marks.

```sql
SELECT 'Hello';
SELECT 'My SQL journey';
```

### 4. SHOW DATABASES
Shows the databases available on the MySQL server.

```sql
SHOW DATABASES;
```

Databases found:

- information_schema
- mysql
- performance_schema
- sakila
- sys
- world

### 5. USE
`USE` selects the database that I want to work with.

```sql
USE world;
```

### 6. SHOW TABLES
Shows the tables inside the currently selected database.

```sql
SHOW TABLES;
```

Tables found in the `world` database:

- city
- country
- countrylanguage

### 7. SELECT * FROM
The `*` means all columns.

```sql
SELECT * FROM city;
```

### 8. LIMIT
`LIMIT` controls how many rows are returned.

```sql
SELECT *
FROM city
LIMIT 5;
```

Another practice:

```sql
SELECT *
FROM city
LIMIT 3;
```

### 9. Selecting One Column
A specific column can be selected instead of using `*`.

```sql
SELECT Name
FROM city
LIMIT 5;
```

### 10. Selecting Multiple Columns
Multiple column names are separated using a comma.

```sql
SELECT Name, Population
FROM city
LIMIT 5;
```

## Important Lessons

- A SQL statement normally ends with a semicolon (`;`).
- Do not use a colon (`:`) instead of a semicolon.
- A column represents a type/category of information.
- A row represents one record.
- `SELECT` retrieves or displays data.
- `FROM` specifies which table the data comes from.
- `*` selects all columns.
- `LIMIT` restricts the number of rows returned.
- Multiple columns can be selected by separating their names with commas.
- In MySQL Workbench, make sure the intended query is selected/current before executing it.

## Mistakes and Learning

### Syntax Error
I initially used a colon instead of a semicolon:

```sql
SELECT 10:
```

This produced MySQL Error 1064.

Correct version:

```sql
SELECT 10;
```

### Workbench Execution
At one point, MySQL Workbench kept showing the previous one-column result.

I learned to make sure the correct query is selected/current before executing it.

## Current Position

**SQL Day 1 is still In Progress.**

The lesson was started on 28 September 2026 and continued on 29 September 2026.

Next SQL session will continue from selecting columns and further basic SQL queries.
