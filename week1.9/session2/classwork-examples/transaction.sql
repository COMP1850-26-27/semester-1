BEGIN;
INSERT INTO orders (order_id, customer_id, restaurant_id) VALUES (5001, 12, 3);
INSERT INTO order_items VALUES (5001, 87, 2);
COMMIT; -- or ROLLBACK; to undo!
