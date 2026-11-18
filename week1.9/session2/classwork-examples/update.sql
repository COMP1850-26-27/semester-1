-- note that we use the primary key to filter for safety when updating!
UPDATE restaurants SET postcode = 'LS6 3QR' WHERE restaurant_id = 1;

-- we can treat attributes like variables and make them use their own values
UPDATE menu_items SET price = price * 1.1 WHERE restaurant_id = 4;