-- SQL Day 3 | 08 Oct 2026
-- Database: world
USE world;

-- Review: filter population
SELECT Name, District, Population
FROM City
WHERE Population > 500000
LIMIT 5;

-- Sort largest to smallest
SELECT Name, Population FROM City
ORDER BY Population DESC LIMIT 5;

-- Sort smallest to largest
SELECT Name, Population FROM City
ORDER BY Population ASC LIMIT 5;

-- Combine WHERE and ORDER BY
SELECT Name, Population FROM City
WHERE Population > 1000000
ORDER BY Population DESC LIMIT 5;

-- Sort by multiple columns
SELECT Name, District, Population FROM City
ORDER BY District ASC, Population DESC LIMIT 10;

-- Unique districts
SELECT DISTINCT District FROM City LIMIT 10;

-- Unique districts alphabetically
SELECT DISTINCT District FROM City
ORDER BY District ASC LIMIT 10;

-- Total cities (observed: 4079)
SELECT COUNT(*) FROM City;

-- Cities above 500,000 (observed: 539)
SELECT COUNT(*) FROM City
WHERE Population > 500000;

-- Number of distinct districts (observed: 1367)
SELECT COUNT(DISTINCT District) FROM City;

-- Final challenge (observed: 200)
SELECT COUNT(DISTINCT District) FROM City
WHERE Population > 1000000;
