# SQL — Day 3 | 08 Oct 2026

**Status:** Lesson and final challenge completed. Full combined `.sql` file prepared; full-script rerun not yet confirmed.

**Database:** MySQL sample `world`, table `City`.

## Concepts
- `ORDER BY Population DESC`: largest to smallest.
- `ORDER BY Population ASC`: smallest to largest.
- `ORDER BY District ASC, Population DESC`: alphabetic district order; within the same district, higher populations first.
- `SELECT DISTINCT District`: return each distinct district value once.
- `COUNT(*)`: count matching rows, including rows with NULL values.
- `COUNT(DISTINCT District)`: count unique non-NULL district values.
- `WHERE` filters rows before the results are counted.
- `LIMIT` limits returned rows; use `ORDER BY` when the chosen first rows must be predictable.

## Verified interactive results
- `SELECT COUNT(*) FROM City` → **4079**
- `COUNT(*) WHERE Population > 500000` → **539**
- `COUNT(DISTINCT District)` → **1367**
- `COUNT(DISTINCT District) WHERE Population > 1000000` → **200**
- `ORDER BY Population DESC LIMIT 5`: Mumbai (Bombay), Seoul, São Paulo, Shanghai, Jakarta.
- `ORDER BY Population ASC LIMIT 5`: Adamstown, West Island, Fakaofo, Città del Vaticano, Bantam.

## Note
Blank strings and nonstandard characters in `District` may sort before alphabetic district names. `DISTINCT` alone does not guarantee sorting.

## Final challenge
```sql
SELECT COUNT(DISTINCT District)
FROM City
WHERE Population > 1000000;
```
Output: **200**.

## Next
SQL Day 4. First, rerun the consolidated Day 3 practice file in MySQL Workbench and verify it completes successfully.
