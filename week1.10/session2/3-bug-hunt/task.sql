-- To un-comment the later tasks remove /* and */.


-- 1
SELECT restaurant_id, r.name
FROM orders o
JOIN restaurants r
  ON o.restaurant_id = r.restaurant_id;


-- 2
/*
SELECT o.order_id, d.name
FROM orders o
JOIN drivers d
  ON o.customer_id = d.driver_id;
  */

-- 3
/*
SELECT o.order_id, c.name
FROM orders o
JOIN customers c;
*/


-- 4
/*
SELECT o.order_id, m.name
FROM orders o
JOIN menu_items m
  ON o.order_id = m.item_id;
  */

-- 5
/*
SELECT r.name, COUNT(*)
FROM orders o
JOIN restaurants r
  ON o.restaurant_id = r.restaurant_id;
  */

