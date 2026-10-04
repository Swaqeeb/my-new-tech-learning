-- SQL — Day 2 | 04 Oct 2026
USE world;

SELECT Name, District, Population FROM city ORDER BY Population DESC LIMIT 5;
SELECT DISTINCT CountryCode FROM city LIMIT 10;
SELECT DISTINCT CountryCode FROM city ORDER BY CountryCode DESC LIMIT 10;
SELECT Name, Population FROM city WHERE Population BETWEEN 500000 AND 1000000 LIMIT 5;
SELECT Name, District, Population FROM city WHERE Population BETWEEN 1000000 AND 2000000 ORDER BY Population DESC LIMIT 5;
SELECT Name, CountryCode, Population FROM city WHERE CountryCode IN ('BGD', 'IND', 'PAK') LIMIT 10;
SELECT Name, CountryCode, Population FROM city WHERE CountryCode IN ('JPN', 'KOR') LIMIT 8;
SELECT Name, CountryCode FROM city WHERE CountryCode NOT IN ('BGD', 'IND', 'PAK') LIMIT 10;
SELECT Name, CountryCode, Population FROM city WHERE CountryCode NOT IN ('USA', 'CHN') ORDER BY Population DESC LIMIT 5;
SELECT Name FROM city WHERE Name LIKE 'A%' LIMIT 10;
SELECT Name FROM city WHERE Name LIKE '%a' LIMIT 10;
SELECT Name FROM city WHERE Name LIKE '%pur%' LIMIT 10;
SELECT Name, CountryCode, Population FROM city WHERE Name LIKE 'S%' ORDER BY Population DESC LIMIT 5;
SELECT Name FROM city WHERE Name LIKE 'L_ma' LIMIT 10;
SELECT Name FROM city WHERE Name NOT LIKE 'A%' LIMIT 5;

-- Final challenge
SELECT Name, CountryCode, Population
FROM city
WHERE Population BETWEEN 1000000 AND 5000000
AND CountryCode NOT IN ('USA', 'CHN')
AND Name NOT LIKE 'A%'
ORDER BY Population DESC
LIMIT 5;
