INSERT INTO restaurants(name, cuisine, postcode, hygiene_rating) VALUES ('Pho Real', 'Vietnamese', 'LS6 3HN', 5);

INSERT INTO restaurants (name, cuisine) VALUES ('Taco Town', 'Mexican');


-- To see just those we can use 'IN'
SELECT * FROM restaurants WHERE name IN ('Taco Town', 'Pho Real');