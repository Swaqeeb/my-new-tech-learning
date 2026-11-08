-- SQL Day 5 revision | 08 November 2026
-- Corrected consolidated practice from the session. SELECT queries only.
-- Individual exercises ran on the learner PC; full-script rerun pending.
USE world;

-- 1. Warm-up: top five cities above one million
SELECT Name, Population
FROM city
WHERE Population > 1000000
ORDER BY Population DESC
LIMIT 5;

-- 2. Count large cities per country
SELECT CountryCode, COUNT(*)
FROM city
WHERE Population > 1000000
GROUP BY CountryCode;

-- 3. Countries with more than five large cities
SELECT CountryCode, COUNT(*)
FROM city
WHERE Population > 1000000
GROUP BY CountryCode
HAVING COUNT(*) > 5;

-- 4. Top three by qualifying city count
SELECT CountryCode, COUNT(*)
FROM city
WHERE Population > 1000000
GROUP BY CountryCode
HAVING COUNT(*) > 5
ORDER BY COUNT(*) DESC
LIMIT 3;

-- 5. Mixed recall: cities above 500000
SELECT CountryCode, COUNT(*)
FROM city
WHERE Population > 500000
GROUP BY CountryCode
HAVING COUNT(*) > 10
ORDER BY COUNT(*) DESC
LIMIT 5;

-- 6. Count all cities and use an alias
SELECT CountryCode, COUNT(*) AS CityCount
FROM city
GROUP BY CountryCode
HAVING COUNT(*) > 100
ORDER BY CityCount DESC;

-- 7. Top five average city populations
SELECT CountryCode, AVG(Population) AS AveragePopulation
FROM city
GROUP BY CountryCode
ORDER BY AveragePopulation DESC
LIMIT 5;

-- 8. Filter country averages
SELECT CountryCode, AVG(Population) AS AveragePopulation
FROM city
GROUP BY CountryCode
HAVING AVG(Population) > 1000000
ORDER BY AveragePopulation DESC;

-- 9. Filter city population totals
SELECT CountryCode, SUM(Population) AS TotalCityPopulation
FROM city
GROUP BY CountryCode
HAVING TotalCityPopulation > 50000000
ORDER BY TotalCityPopulation DESC;

-- 10. Largest city population per country
SELECT CountryCode, MAX(Population) AS LargestCityPopulation
FROM city
GROUP BY CountryCode
ORDER BY LargestCityPopulation DESC
LIMIT 5;

-- 11. Final mixed challenge
SELECT CountryCode, COUNT(*) AS CityCount, SUM(Population) AS TotalCityPopulation
FROM city
GROUP BY CountryCode
HAVING CityCount > 100
ORDER BY TotalCityPopulation DESC;

