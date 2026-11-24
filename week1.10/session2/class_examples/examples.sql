-- Joins

SELECT orders.order_id, customers.name
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id limit 5 offset 49;

-- This will get an error:

--SELECT restaurant_id, name
--FROM orders
--JOIN restaurants
--  ON orders.restaurant_id = restaurants.restaurant_id;

-- This works:

SELECT o.restaurant_id, r.name
FROM orders o
JOIN restaurants r
  ON o.restaurant_id = r.restaurant_id;
