-- SQL — Day 1 | 30 Sep 2026
-- Topic: SQL Basics, SELECT, WHERE, Comparison Operators, AND, OR


-- ==========================================
-- 1. Basic SELECT
-- ==========================================

SELECT 10;

SELECT 25;

SELECT 10 + 5;

SELECT 'Hello';

SELECT 'My SQL journey';


-- ==========================================
-- 2. View Databases
-- ==========================================

SHOW DATABASES;


-- ==========================================
-- 3. Select the World Database
-- ==========================================

USE world;


-- ==========================================
-- 4. View Tables
-- ==========================================

SHOW TABLES;


-- ==========================================
-- 5. Display Rows from City
-- ==========================================

SELECT *
FROM City
LIMIT 5;

SELECT *
FROM City
LIMIT 3;


-- ==========================================
-- 6. Select Specific Columns
-- ==========================================

SELECT Name
FROM City
LIMIT 5;

SELECT Name, Population
FROM City
LIMIT 5;

SELECT Name, District
FROM City
LIMIT 3;


-- ==========================================
-- 7. WHERE with Text
-- ==========================================

SELECT Name, District
FROM City
WHERE District = 'Kabol';


-- ==========================================
-- 8. WHERE with Greater Than
-- ==========================================

SELECT Name, Population
FROM City
WHERE Population > 1000000;


-- ==========================================
-- 9. WHERE with Less Than
-- ==========================================

SELECT Name, Population
FROM City
WHERE Population < 500000
LIMIT 5;


-- ==========================================
-- 10. Greater Than or Equal To
-- ==========================================

SELECT Name, Population
FROM City
WHERE Population >= 1000000
LIMIT 5;


-- ==========================================
-- 11. Less Than or Equal To
-- ==========================================

SELECT Name, Population
FROM City
WHERE Population <= 200000
LIMIT 5;


-- ==========================================
-- 12. Not Equal To
-- ==========================================

SELECT Name, District
FROM City
WHERE District != 'Kabol'
LIMIT 5;


-- ==========================================
-- 13. AND
-- ==========================================

SELECT Name, Population
FROM City
WHERE Population > 500000
AND Population < 1000000
LIMIT 5;


-- ==========================================
-- 14. Independent AND Practice
-- ==========================================

SELECT Name, Population
FROM City
WHERE Population >= 200000
AND Population <= 300000
LIMIT 5;


-- ==========================================
-- 15. OR
-- ==========================================

SELECT Name, District
FROM City
WHERE District = 'Kabol'
OR District = 'Herat';


-- ==========================================
-- 16. Final Day 1 Challenge
-- ==========================================

SELECT Name, District, Population
FROM City
WHERE Population >= 500000
AND Population <= 1000000
LIMIT 5;


-- ==========================================
-- Day 1 Quick Reference
-- ==========================================

-- SELECT  -> choose what information to display
-- FROM    -> choose the table
-- WHERE   -> filter rows
-- LIMIT   -> limit the number of returned rows

-- =   -> equal to
-- !=  -> not equal to
-- >   -> greater than
-- <   -> less than
-- >=  -> greater than or equal to
-- <=  -> less than or equal to

-- AND -> both conditions must be true
-- OR  -> at least one condition must be true
