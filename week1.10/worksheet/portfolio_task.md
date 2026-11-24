# Week 10 Portfolio Task

Write 5 SQL queries on the Aire Bikes database. **Your query passes only if its output exactly matches the correct answer**, so read each task carefully!

## The database

Aire Bikes is the same city bike-hire scheme as last week's quiz. It has four tables:

| Table | Columns |
| --- | --- |
| `members` | `member_id`, `first_name`, `last_name`, `membership`, `joined` |
| `bikes` | `bike_id`, `bike_type`, `year_added` |
| `stations` | `station_id`, `name`, `area`, `capacity` |
| `trips` | `trip_id`, `member_id`, `bike_id`, `start_station`, `end_station`, `start_time`, `duration_mins`, `cost` |

A database diagram is provided to help you consider joins.

## How your queries are marked

Your output must have:

- the right rows: no missing rows and no extra rows
- the right columns, in the order the task lists them. Column names don't matter, so `AS` is fine!
- the right values. Round only when the task says so!
- the right order (including the tie-break when the task gives one)

## How to submit

In the provided `task.sql` file, you will find comments `-- W1` etc. You should write the query for each numbered question below under the comment with its number.

You can also do this in separate files, which must be named **exactly** `W1.sql` etc.


## Tasks

1.  Trips by membership type

For each membership type, show:

1. the membership type
2. the number of trips taken
3. the total cost of those trips, rounded to 2 decimal places

Show the membership type with **the most trips first**.

---

2. Frequent riders

For every member who has taken more than 10 trips, show:

1. their first name
2. their last name
3. their number of trips

Show the member with **the most trips first**. If two members have the same number of trips, sort them by **last name, A to Z**.

---

3. The longest trips

For every trip longer than 60 minutes, show:

1. the trip ID
2. the last name of the member who took it
3. the name of the station it **started** from
4. its duration in minutes

Show **the longest trip first**.

---

4. Busy stations in November

For every station where more than 5 trips started in November 2026, show:

1. the station's name
2. the number of trips that started there in November 2026

Show **the busiest station first**. If two stations have the same number of trips, sort them by **station name, A to Z**.

---

5. Electric Bike - Biggest Spenders.

For every member who has spent more than £50 in total on trips using electric bikes, show:

1. their last name
2. that total, rounded to 2 decimal places

Show **the biggest spender first**.

## Tips

- Build up in steps. Start with the join, run it and check the rows. Then add WHERE, then GROUP BY, then HAVING, then ORDER BY.
- "More than" means `>`, not `>=`.
- Dates are stored as text- `'2026-11-02 18:30'`, so `LIKE '2026-09%'` would find all dates in September.
- Check your columns against the numbered list in each task before you submit.