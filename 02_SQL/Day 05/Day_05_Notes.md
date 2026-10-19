# SQL — Day 5 | 19 October 2026

**Track:** My Tech Learning Journey — SQL  
**Database:** MySQL `world`  
**Table:** `City`  
**Status:** Core lesson completed. Independent `WHERE` + `GROUP BY` + `HAVING` challenge and spaced-recall mastery check pending.

## 1. Review of older concepts

- `SELECT Name, Population` chooses columns to display.
- `WHERE Population > 1000000` filters individual city rows.
- `ORDER BY Population DESC` sorts populations highest to lowest. `ASC` means lowest to highest.
- `LIMIT 5` returns up to five rows.
- `COUNT(*)` counts rows.

**Recall exercise completed:** Find the five highest-population cities above one million. Results were Mumbai (Bombay) 10,500,000; Seoul 9,981,619; São Paulo 9,968,485; Shanghai 9,696,300; Jakarta 9,604,900. The learner needed a reminder for `ORDER BY ... DESC` and fixed the typo `Pupulation` → `Population`.

## 2. GROUP BY

`GROUP BY CountryCode` places cities with the same `CountryCode` into a group. `COUNT(*)` then counts the rows in each group.

```sql
SELECT CountryCode, COUNT(*)
FROM City
GROUP BY CountryCode;
```

**Small example:** BGD with three listed cities and IND with two listed cities yields two result rows: BGD = 3, IND = 2. These are illustrative example counts, not results from the complete database.

**Real database result reported:** Bangladesh (`BGD`) has 24 rows recorded in the sample `City` table.

## 3. Order grouped results by their counts

```sql
SELECT CountryCode, COUNT(*)
FROM City
GROUP BY CountryCode
ORDER BY COUNT(*) DESC
LIMIT 5;
```

**Verified user-reported results:** CHN 363; IND 341; USA 274; BRA 250; JPN 248.

**Important distinction:** `ORDER BY CountryCode DESC` sorts codes in reverse alphabetical order, whereas `ORDER BY COUNT(*) DESC` sorts groups by their city count.

## 4. WHERE before grouping

```sql
SELECT CountryCode, COUNT(*)
FROM City
WHERE Population > 1000000
GROUP BY CountryCode;
```

`WHERE` first removes cities whose population is not above one million; then `GROUP BY` groups the remaining cities and `COUNT(*)` counts them. The user independently wrote and ran this query. The supplied results included BGD = 2, ARG = 3 and AUS = 4.

**More complex exercise completed:**

```sql
SELECT CountryCode, COUNT(*)
FROM City
WHERE Population > 1000000
GROUP BY CountryCode
ORDER BY COUNT(*) DESC
LIMIT 5;
```

**Verified user-reported results:** CHN 35; IND 18; BRA 13; RUS 12; JPN 11.

## 5. HAVING filters groups

`WHERE` filters individual rows *before* grouping; `HAVING` filters aggregate groups *after* grouping.

```sql
SELECT CountryCode, COUNT(*)
FROM City
GROUP BY CountryCode
HAVING COUNT(*) > 50;
```

The query was practiced. The user pasted RUS 189, TUR 62, UKR 57, USA 274 — a **partial** result set, not necessarily the full output.

You cannot use `WHERE COUNT(*) > 50` in place of `HAVING COUNT(*) > 50`: `WHERE` evaluates individual rows before the group count exists, whereas `HAVING` can test aggregate values.

The typical clause order:

```text
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

## 6. Remaining independent challenge — NOT YET COMPLETED

**Manager request:** “Show the country codes and city counts for countries that have more than five cities with populations greater than one million.”

Write the SQL yourself, using `WHERE Population > 1000000`, `GROUP BY CountryCode`, and `HAVING COUNT(*) > 5`. Execute it, save the result, then explain why the two filters cannot be swapped.

## 7. Personal error and recall log

| Issue | Learning point | Retest |
|---|---|---|
| Forgot sorting syntax | `ORDER BY <column> DESC` | Next session, 3-day and 7-day recall |
| Typo `Pupulation` | Column names must be spelled correctly | Next session |
| Misspelled `Contrycode` | Use actual column name `CountryCode` | Next session |
| Used `SELECT BGD` and `GROUP BY BGD` | `'BGD'` is a value; `CountryCode` is a column | Next session |
| Sorted by `CountryCode DESC` instead of count | Sort by `COUNT(*) DESC` for largest groups | 3-day recall |
| Initially omitted `GROUP BY` and `DESC` | Check requirements and clause order | 3-day recall |
| HAVING vs WHERE | WHERE filters rows, HAVING filters groups | Next session |

## 8. Mastery and next steps

- **Core lesson:** completed 19 Oct 2026.
- **Independent final HAVING query:** pending.
- **Long-term mastery:** pending; revisit without notes after ~1, ~3, and ~7 days.
- **Practice file:** `Day_05_Practice.sql` includes completed queries plus a clearly marked pending challenge.
- After the practice file is tested in MySQL Workbench, save the files locally and commit/push to GitHub. A Drive upload does not mean the files are in GitHub.
