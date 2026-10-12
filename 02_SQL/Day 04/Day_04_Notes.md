# SQL — Day 4 | 12 October 2026

**Learning status:** Day 4 lesson and final challenge completed. Consolidated SQL file has been prepared, but a full-file rerun and the *additional* exercises remain pending.

**Environment:** MySQL Workbench; sample database `world`; table `City`.

## Four aggregate functions
| Function | Purpose | Observed MySQL result |
|---|---|---:|
| `MAX(Population)` | Largest city population | 10,500,000 |
| `MIN(Population)` | Smallest city population | 42 |
| `SUM(Population)` | Total of city population values | 1,429,559,884 |
| `AVG(Population)` | Average population value | 350,468.2236 |

`AVG(Population) WHERE Population > 1000000` was **2,422,519.9072**.

The independent final challenge was to find the maximum population among cities below 500,000. Correct query:

```sql
SELECT MAX(Population)
FROM City
WHERE Population < 500000;
```

**Verified result: 497,464.** First attempt used `< 5000000` by mistake, which ran but answered the wrong question; the user identified and corrected the extra zero.

## Concepts to remember
- `WHERE` restricts rows **before** the aggregate is evaluated.
- `MAX` finds the largest qualifying value; `MIN` finds the smallest.
- `SUM` adds qualifying values; `AVG` computes their arithmetic mean.
- Aggregate results describe records in the dataset, not necessarily the entire real-world population.
- A valid SQL query can still produce an incorrect business answer if its filter is wrong.
- Most aggregate functions ignore `NULL` values; check whether columns contain `NULL` when interpreting outputs.

## Improved professional practice strategy (applies to SQL and Python from the next lesson)
1. Explain each concept and where it is used at work.
2. Complete **2–3 easy exercises**, then **2 medium exercises**.
3. Complete **1 complex/mixed problem**, **1 debugging task**, and **1 realistic workplace challenge** per concept or tightly related cluster.
4. Predict outputs, write code/queries independently, then execute and explain why the result is correct.
5. Review material from the previous lesson at the beginning of the next session, and revisit after 2–3 days and a week.
6. Track recurring mistakes and revisit them until resolved. Do not mark an exercise complete until the user verifies its output.
7. Keep lessons bite-sized: one step and feedback at a time. Number of exercises may be adjusted for the topic.

## Additional practice — pending
The `Day_04_Practice.sql` file includes **new easy, medium, debugging and workplace exercises** to reinforce the Day 4 concepts. These are not yet completed. Work through them before SQL Day 5, or as an opening revision.

## Next
Run the consolidated Day 4 script and verify its output; complete extra exercises, save local/GitHub copies, then SQL Day 5 (`GROUP BY` when ready).
