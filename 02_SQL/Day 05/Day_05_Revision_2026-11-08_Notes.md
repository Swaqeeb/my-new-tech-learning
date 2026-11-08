# SQL — Day 5 revision | 08 November 2026

## Session outcome
Practice completed using MySQL Workbench and the world.City table. Query/output evidence was supplied in chat. This is revision of SQL Day 5, not a restart of SQL Day 1. Independent retained mastery is not yet confirmed. Python remains Day 19 complete; next Python is Day 20.

## Concepts and when to use them
| Tool | Use |
|---|---|
| COUNT(*) | Count city rows in each group |
| SUM(Population) | Add recorded city populations |
| AVG(Population) | Average recorded city populations |
| MAX(Population) | Find the largest recorded city population |
| GROUP BY CountryCode | Produce a separate calculation for each country |
| WHERE | Filter individual rows before aggregation |
| HAVING | Filter grouped results after aggregation |
| AS | Give the result column a readable name; does not calculate anything |
| ORDER BY ... DESC | Sort largest first |
| LIMIT | Restrict the number of output rows after sorting |

Write clauses in this order: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT. Omit clauses the task does not need. MySQL allows the SELECT alias in HAVING and ORDER BY.

## Important distinction
WHERE Population > 1000000 removes smaller cities before calculating an average. HAVING AVG(Population) > 1000000 averages all recorded cities per country, then keeps countries whose average exceeds one million. City-table totals are totals of the recorded cities, not national population totals.

## Practice evidence
- Top three countries by count of cities above one million: CHN 35, IND 18, BRA 13.
- Top five counts above 500000: CHN 62, IND 50, RUS 33, BRA 29, USA 29. Equal counts may appear in either order without a secondary sort key.
- Average above one million: SGP 4017733; HKG 1650316.5; URY 1236000; GIN 1090610.
- Largest city population: IND 10500000; KOR 9981619; BRA 9968485; CHN 9696300; IDN 9604900.
- Final query used COUNT and SUM together, HAVING CityCount > 100, and descending total population. The learner requested a COUNT reminder before completing it.

## Final verified output
| CountryCode | CityCount | TotalCityPopulation |
|---|---:|---:|
| CHN | 363 | 175953614 |
| IND | 341 | 123298526 |
| BRA | 250 | 85876862 |
| USA | 274 | 78625774 |
| JPN | 248 | 77965107 |
| RUS | 189 | 69150700 |
| MEX | 173 | 59752521 |
| PHL | 136 | 30934791 |

## Error log and next retest
| Mistake | Correction | Next check |
|---|---|---|
| Forgot grouping | GROUP BY CountryCode gives one calculation per country | Next SQL session |
| Used Population AS to calculate total/average | Use SUM or AVG; AS only labels | Next SQL session |
| Used WHERE to filter an average | Use HAVING after GROUP BY | Next SQL session |
| Sorted by count,Population | Sort by COUNT(*) or its alias | Next SQL session |
| Typed Populaiton | Correct spelling is Population | Every run |
| Pasted previous query output | Select and execute the intended query, then check headings/results | Every run |

## Next learning checkpoint
Begin with one fresh task combining a row filter, grouping, an aggregate condition, and ordering, without a template. Use progressive hints if needed. Then progress to SQL Day 6 when the learner can explain WHERE versus HAVING and choose the aggregate. Repeat brief recall around 09, 11 and 15 November, or the next available sessions; these are study targets, not scheduled notifications.

## Records
The companion SQL file contains corrected consolidated queries, not an exact export of the Workbench tab. Individual exercise results are verified from chat; full-script rerun is pending. Today’s Drive and GitHub synchronization must be tracked separately and confirmed after saving/pushing.
