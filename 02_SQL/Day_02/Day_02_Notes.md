# SQL — Day 2 | 04 Oct 2026

## Status
COMPLETED

## Topics Learned
ORDER BY; ASC/DESC; DISTINCT; BETWEEN; IN; NOT IN; LIKE; wildcards % and _; NOT LIKE; multiple WHERE conditions with AND; LIMIT with sorting/filtering.

## Key Examples

### ORDER BY
```sql
SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 5;
```
ASC = smallest to largest / A to Z. DESC = largest to smallest / Z to A.

### DISTINCT
```sql
SELECT DISTINCT CountryCode
FROM city
LIMIT 10;
```
Returns unique values.

### BETWEEN
```sql
SELECT Name, Population
FROM city
WHERE Population BETWEEN 500000 AND 1000000
LIMIT 5;
```
BETWEEN includes both boundaries.

### IN / NOT IN
```sql
WHERE CountryCode IN ('BGD', 'IND', 'PAK')
WHERE CountryCode NOT IN ('USA', 'CHN')
```

### LIKE / NOT LIKE
```sql
WHERE Name LIKE 'A%'      -- starts with A
WHERE Name LIKE '%a'      -- ends with a
WHERE Name LIKE '%pur%'   -- contains pur
WHERE Name LIKE 'L_ma'    -- _ = exactly one character
WHERE Name NOT LIKE 'A%'  -- does not start with A
```
% = zero or more characters. _ = exactly one character.

## Important Lessons
- DISTINCT removes duplicates; DESC controls descending sorting.
- DESC belongs with ORDER BY.
- Check numeric zeros carefully in BETWEEN ranges.
- Use one WHERE and connect additional filters with AND/OR.
- LIMIT restricts rows; it does not guarantee every value listed in IN appears.
- Read column spelling carefully (Population).

## Final Challenge — Successful
```sql
SELECT Name, CountryCode, Population
FROM city
WHERE Population BETWEEN 1000000 AND 5000000
AND CountryCode NOT IN ('USA', 'CHN')
AND Name NOT LIKE 'A%'
ORDER BY Population DESC
LIMIT 5;
```

Result:
Santiago de Chile | CHL | 4703954
St Petersburg | RUS | 4694000
Calcutta [Kolkata] | IND | 4399819
Baghdad | IRQ | 4336000
Singapore | SGP | 4017733

## Retention
Sort → ORDER BY
Largest first → DESC
Unique → DISTINCT
Range → BETWEEN
One of values → IN
Exclude values → NOT IN
Text pattern → LIKE
Exclude pattern → NOT LIKE
