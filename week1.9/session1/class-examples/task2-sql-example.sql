.headers on
.mode column

-- count the orders which Amara Okafor made from Italian restaurants

SELECT COUNT(*) FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN restaurants r ON o.restaurant_id = r.restaurant_id WHERE c.name = 'Amara Okafor' AND r.cuisine = 'Italian';


-- Update the postcode

UPDATE restaurants SET postcode = 'LS6 3QR' WHERE name = 'Bella Napoli';