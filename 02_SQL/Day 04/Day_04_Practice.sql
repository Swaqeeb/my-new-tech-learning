-- SQL Day 4 | 12 Oct 2026
-- Database: MySQL world / City
-- PART A: Queries already practiced and verified interactively
USE world;

-- 1. Largest city population: 10500000
SELECT MAX(Population) AS largest_population FROM City;

-- 2. Smallest city population: 42
SELECT MIN(Population) AS smallest_population FROM City;

-- 3. Total recorded population: 1429559884
SELECT SUM(Population) AS total_population FROM City;

-- 4. Average population: 350468.2236 (Workbench output)
SELECT AVG(Population) AS average_population FROM City;

-- 5. Average for cities with more than one million people: 2422519.9072
SELECT AVG(Population) AS avg_large_city_population FROM City
WHERE Population > 1000000;

-- 6. Final challenge: maximum among cities under 500000: 497464
SELECT MAX(Population) AS max_under_500k FROM City
WHERE Population < 500000;

-- PART B: NEW INDEPENDENT PRACTICE (not yet completed or verified)
-- Read Day_04_Notes.md and write queries below; do not look up solutions first.
-- E1: Find the smallest population among cities over 100000 people.
-- E2: Find the total population of cities in district 'Dhaka' (if present).
-- E3: Find the average population of cities below 100000 people.
-- M1: Return minimum, maximum and average population in one row.
-- M2: Return sum and average population for cities > 500000.
-- M3: Find minimum population among cities between 100000 and 500000 (exclusive).
-- D1: Debug this intentionally incorrect query (MAX among cities below 500000):
--     SELECT MAX(Population) FROM City WHERE Population < 5000000;
-- R1: IT manager asks for the maximum and average population of cities with Population >= 250000;
--     write one query returning both figures with clear aliases.
-- R2: Explain why SUM(Population) of City is not necessarily the world's population.
-- Run each completed query and record its output in your own practice log.
