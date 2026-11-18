.headers on
.mode column


-- Some examples of order by and limit - unlimited are commented out, to run those remove the '--'
-- they will have lots of results!

-- SELECT name, price from menu_items ORDER BY price DESC;

SELECT name, price from menu_items ORDER BY price DESC LIMIT 5;

-- SELECT name, price from menu_items ORDER BY price ASC;

SELECT name, price from menu_items ORDER BY price ASC LIMIT 5;
