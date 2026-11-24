
-- slide 18
SELECT ROUND(AVG(price), 2) AS avg_price FROM menu_items;

-- slide 20
SELECT restaurant_id, COUNT(*)
FROM menu_items;

SELECT restaurant_id, COUNT(*)
FROM menu_items
GROUP BY restaurant_id;

-- slide 21
SELECT COUNT(*), COUNT(driver_id)
FROM orders;

-- slide 22 answers

-- we count the number of items per restaurant ID, and then for readability sort it ascending and limit 1 - if this isn't '1' we have disproved the diagram.
SELECT restaurant_id, count(*) AS num_items from menu_items
GROUP BY restaurant_id
ORDER BY num_items ASC LIMIT 1;

-- we count the number of reviews per order id, order desc, and limit 5 for readability. If this showed more than '1' we would have disproved.
SELECT order_id, count(*) AS num_reviews FROM reviews
GROUP BY order_id
ORDER BY num_reviews DESC LIMIT 5;

-- not really a proof, but we can count each of these:
SELECT count(*) AS total_orders FROM orders;
select count(driver_id) AS has_driver FROM orders;
select count(*) AS no_driver FROM orders WHERE driver_id IS NULL;

-- slide 24
SELECT restaurant_id, COUNT(*) AS veg_items
FROM menu_items
WHERE is_vegetarian = 1
GROUP BY restaurant_id;

SELECT restaurant_id, COUNT(*) AS total_orders
FROM orders
GROUP BY restaurant_id
HAVING total_orders < 20;

-- slide 25
SELECT restaurant_id, ROUND(AVG(price), 2) AS avg_price
FROM menu_items
WHERE is_vegetarian = 1
GROUP BY restaurant_id
HAVING COUNT(*) >= 3
ORDER BY avg_price DESC
LIMIT 5;
