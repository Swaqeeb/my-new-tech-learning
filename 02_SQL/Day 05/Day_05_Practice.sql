-- SQL — Day 5 | 19 October 2026
-- GROUP BY, WHERE, COUNT(*), ORDER BY and HAVING
-- All queries in SECTION A are based on lesson exercises.
-- Run them in MySQL Workbench to verify the consolidated script.
-- SECTION B is uncompleted independent practice; write your own solution.

USE world;

-- A1. Recall: five largest cities with population above one million
SELECT Name, Population
FROM City
WHERE Population > 1000000
ORDER BY Population DESC
LIMIT 5;

-- A2. Count all cities per country
SELECT CountryCode, COUNT(*) AS city_count
FROM City
GROUP BY CountryCode;

-- A3. Count only Bangladesh cities (reported result: 24)
SELECT COUNT(*) AS bangladesh_city_count
FROM City
WHERE CountryCode = 'BGD';

-- A4. Top five countries by total recorded city count
-- Reported results: CHN 363, IND 341, USA 274, BRA 250, JPN 248
SELECT CountryCode, COUNT(*) AS city_count
FROM City
GROUP BY CountryCode
ORDER BY COUNT(*) DESC
LIMIT 5;

-- A5. Count only cities above one million, grouped by country
SELECT CountryCode, COUNT(*) AS large_city_count
FROM City
WHERE Population > 1000000
GROUP BY CountryCode;

-- A6. Top five countries by count of cities above one million
-- Reported results: CHN 35, IND 18, BRA 13, RUS 12, JPN 11
SELECT CountryCode, COUNT(*) AS large_city_count
FROM City
WHERE Population > 1000000
GROUP BY CountryCode
ORDER BY COUNT(*) DESC
LIMIT 5;

-- A7. Countries with more than 50 cities
SELECT CountryCode, COUNT(*) AS city_count
FROM City
GROUP BY CountryCode
HAVING COUNT(*) > 50;

-- SECTION B — PENDING INDEPENDENT CHALLENGE (not yet solved/verified)
-- Manager: Show country codes and counts for countries that have
-- more than FIVE cities with populations greater than ONE MILLION.
-- Write your own query below, then run and send the output.
-- Hints only if needed: WHERE filters cities; HAVING filters grouped counts.

-- SECTION C — LATER RECALL (do not use notes first)
-- 1. Retrieve the three countries with most city records.
-- 2. Count qualifying cities above two million for each country.
-- 3. Debug: Explain why ORDER BY CountryCode DESC is not suitable
--    when the manager asks for countries with the most cities.
