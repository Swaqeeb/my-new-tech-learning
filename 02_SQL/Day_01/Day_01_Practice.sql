-- SQL — Day 1 Practice
-- Started: 28 September 2026
-- Continued: 29 September 2026
-- Status: In Progress


-- 1. Display a number
SELECT 10;


-- 2. Display another number
SELECT 25;


-- 3. Perform a simple calculation
SELECT 10 + 5;


-- 4. Display text
SELECT 'Hello';


-- 5. Independent text practice
SELECT 'My SQL journey';


-- 6. Show available databases
SHOW DATABASES;


-- 7. Select the world database
USE world;


-- 8. Show tables in the selected database
SHOW TABLES;


-- 9. Display the first 5 rows from the city table
SELECT *
FROM city
LIMIT 5;


-- 10. Display the first 3 rows from the city table
SELECT *
FROM city
LIMIT 3;


-- 11. Select one column
SELECT Name
FROM city
LIMIT 5;


-- 12. Select multiple columns
SELECT Name, Population
FROM city
LIMIT 5;


-- Important lessons:
-- SQL statements normally end with a semicolon (;), not a colon (:).
-- Multiple columns are separated using commas.
-- Make sure the intended query is selected/current in MySQL Workbench
-- before executing it.


-- SQL Day 1 will continue in the next SQL session.
