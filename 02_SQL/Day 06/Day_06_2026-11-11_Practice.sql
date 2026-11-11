-- SQL Day 6 | 11 November 2026
-- INNER JOIN, filtering, sorting and limits
-- Corrected consolidation of today's exercises. Read-only queries.
USE world;

-- 1. Recall: countries with over 100 recorded cities
SELECT CountryCode, COUNT(*) AS CityCount
FROM city
GROUP BY CountryCode
HAVING COUNT(*) > 100
ORDER BY CityCount DESC;

-- 2. First INNER JOIN: five matching rows, no guaranteed order
SELECT city.Name AS CityName, country.Name AS CountryName,
       city.Population
FROM city
INNER JOIN country ON city.CountryCode = country.Code
LIMIT 5;

-- 3. Five most populated recorded cities
SELECT city.Name AS CityName, country.Name AS CountryName,
       city.Population
FROM city
INNER JOIN country ON city.CountryCode = country.Code
ORDER BY city.Population DESC
LIMIT 5;

-- 4. All recorded cities in Bangladesh
SELECT city.Name AS CityName, country.Name AS CountryName,
       city.Population
FROM city
INNER JOIN country ON city.CountryCode = country.Code
WHERE country.Name = 'Bangladesh'
ORDER BY city.Population DESC;

-- 5. Five most populated recorded cities in India
SELECT city.Name AS CityName, country.Name AS CountryName,
       city.Population
FROM city
INNER JOIN country ON city.CountryCode = country.Code
WHERE country.Name = 'India'
ORDER BY city.Population DESC
LIMIT 5;

-- 6. Indian cities above three million
SELECT city.Name AS CityName, country.Name AS CountryName,
       city.Population
FROM city
INNER JOIN country ON city.CountryCode = country.Code
WHERE country.Name = 'India' AND city.Population > 3000000
ORDER BY city.Population DESC;

-- 7. Bangladesh cities above two hundred thousand
SELECT city.Name AS CityName, country.Name AS CountryName,
       city.Population
FROM city
INNER JOIN country ON city.CountryCode = country.Code
WHERE country.Name = 'Bangladesh' AND city.Population > 200000
ORDER BY city.Population DESC;

-- 8. Three most populated recorded cities in Japan
SELECT city.Name AS CityName, country.Name AS CountryName,
       city.Population
FROM city
INNER JOIN country ON city.CountryCode = country.Code
WHERE country.Name = 'Japan'
ORDER BY city.Population DESC
LIMIT 3;
