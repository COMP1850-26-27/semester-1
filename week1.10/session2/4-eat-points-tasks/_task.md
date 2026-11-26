# Eat Points: the launch review

Eat Points has been running for a few weeks, and the ops manager wants a review before the board meeting. Work through the sections in order. Each one uses SQL from a different session, and the last two sections are stretch and challenge.

Use the standard `leeds_eats.db` with the loyalty tables (`loyalty_accounts`, `rewards`, `reward_transactions`). Save your queries in `eat_points.sql` and write any text answers in comments (`-- `).

1. List the rewards that cost 300 points or fewer, cheapest first.

2. How many loyalty accounts were created in November 2026?

3. Leeds Eats is adding a new reward: *Free garlic bread*, costing 150 points, for bronze members and above. Add it.

4. The customer with loyalty account 5 has moved up to silver. Update their account. Run a `SELECT` before and after to check it worked.

5. Try to set loyalty account 6's tier to `'platinum'`. What happens, and which part of the table design causes it?

6. What is the total number of points spent across all reward transactions? And the average points per transaction, to 1 decimal place?

7. Which tiers have more than 10 accounts? Show only those tiers.

8. Show the names of all customers with a gold account.

9. For each reward, show its name, how many times it has been used, and the total points spent on it. Most popular first.

10. Show every reward transaction with the reward's name and the time of the order it was used on.

## Stretch

11. Which customers have spent more than 500 points in total? Show their names and the total, highest first.

12. The rules say a reward can only be used by accounts at or above its `tier_required`. Write a query that finds any reward transactions that break this rule. *Hint: start from `reward_transactions` and join your way to both the reward and the customer's loyalty account. Think carefully about how to compare tiers*.

13. Points earned aren't stored anywhere, so the manager has given you a rule: every order placed on or after the day an account was created earns 50 points.

    1. Write a query that shows, for each account, the points it has earned.
    2. Write a second query that shows, for each account, the points it has spent.
    3. Compare the two for at least three accounts. Has anyone spent more points than they earned? What does that tell you about the data, and should the database stop it from happening?

14. The manager wants to see the history of each account's tier: when it moved from bronze to silver, and when it reached gold. The current design only stores the current tier.

    1. Sketch the change to the ERD. Which entity and relationship would you add, and with what multiplicity?
    2. Write the `CREATE TABLE` statement for any new table, with its primary and foreign keys.