# Task 5: Leeds Eats task sheet

Open the database with `sqlite3 leeds_eats.db`, write your queries in `task.sql`, and run them with `.read task.sql`.

Most of these are requests from real people at Leeds Eats. For each one, work out which table and columns you need, then write the query. Some questions also ask you to explain or justify: write your answer as a comment in task.sql, starting with `--`.

Start wherever suits you, and come back to finish off anything you missed in your independent study time.


## Bronze: warm-up

1. List every column for every driver.

2. List the name and price of every dish sold by Bangkok Garden (restaurant 3).

3. List the names of all the Indian restaurants.

4. How many customers does Leeds Eats have?


## Silver: requests from customers and staff

5. **A student:** "I'm vegetarian and I've only got £8. What could I order? Cheapest first, please."

6. **A food safety officer from Leeds City Council:** "Which restaurants have a hygiene rating below 4? Show the worst first."

7. **A student who lives in LS6:** "Which restaurants are near me, best rated first?" Does a matching postcode really mean a restaurant is near? What could go wrong?

8. **The marketing team:** "We want to email everyone who signed up with a University of Leeds email address, newest members first." Write the query, then say whether Leeds Eats should actually send this email.

9. **The operations manager:** "Show me the 10 most recent cancelled orders."

10. **The owner of Pasta Pronto (restaurant 4):** "Which of my dishes are vegetarian? And what's my most expensive dish?" (Two queries.)


## Gold: think it through

11. **The operations manager:** "Some orders from October look stuck: they still say 'placed'. Find them for the support team." Choose only the columns a support agent would need, and justify each one.

12. **A colleague:** "I want the 5 cheapest vegetarian dishes. My first query gives an error and my second gives the wrong answer. Why?"
   
       SELECT name, price FROM menu_items ORDER BY price LIMIT 5 WHERE is_vegetarian = 1;
       SELECT name, price FROM menu_items WHERE is_vegetarian = 1 LIMIT 5;
   
   Explain what's wrong with each, then write a correct version.

13. **A customer:** "What's the cheapest thing I can get on Leeds Eats?" Write the query. Then run it again with LIMIT 5 instead of LIMIT 1. What do you notice, and how should Leeds Eats answer this customer fairly?

14. **The product team:** "We're thinking of launching a 'late-night favourites' menu. How many orders are placed at 21:00 or later, out of all orders?" Is that enough evidence to launch the feature? What else would you want to know?

15. **You:** Think of a question a Leeds Eats customer, restaurant owner or manager might ask. Write it as a request in their words, then write the query. Swap with a neighbour: answer theirs, and check each other's.

