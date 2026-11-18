PRAGMA foreign_keys = ON;

CREATE TABLE customers (
    customer_id  INTEGER PRIMARY KEY,
    name         TEXT NOT NULL,
    email        TEXT NOT NULL UNIQUE,
    postcode     TEXT,
    phone        TEXT,                -- optional, may be NULL
    joined_date  TEXT,                -- 'YYYY-MM-DD'
    referred_by  INTEGER,             -- who referred this customer (NULL if nobody)
    FOREIGN KEY (referred_by) REFERENCES customers(customer_id)
);

CREATE TABLE restaurants (
    restaurant_id  INTEGER PRIMARY KEY,
    name           TEXT NOT NULL,
    cuisine        TEXT,
    postcode       TEXT,
    hygiene_rating INTEGER CHECK (hygiene_rating BETWEEN 0 AND 5)
);

CREATE TABLE menu_items (
    item_id        INTEGER PRIMARY KEY,
    restaurant_id  INTEGER NOT NULL,
    name           TEXT NOT NULL,
    price          REAL CHECK (price > 0),
    is_vegetarian  INTEGER CHECK (is_vegetarian IN (0, 1)),  -- 1 = yes, 0 = no
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

CREATE TABLE drivers (
    driver_id  INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    vehicle    TEXT DEFAULT 'bike',
    phone      TEXT
);

CREATE TABLE orders (
    order_id       INTEGER PRIMARY KEY,
    customer_id    INTEGER NOT NULL,
    restaurant_id  INTEGER NOT NULL,
    driver_id      INTEGER,           -- NULL until a driver is assigned
    order_time     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M', 'now')),  -- 'YYYY-MM-DD HH:MM'
    status         TEXT DEFAULT 'placed'
                   CHECK (status IN ('placed', 'preparing', 'out for delivery', 'delivered', 'cancelled')),
    delivery_fee   REAL,
    FOREIGN KEY (customer_id)   REFERENCES customers(customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (driver_id)     REFERENCES drivers(driver_id)
);

CREATE TABLE order_items (
    order_id  INTEGER,
    item_id   INTEGER,
    quantity  INTEGER CHECK (quantity > 0),
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id)  REFERENCES menu_items(item_id)
);

CREATE TABLE reviews (
    review_id  INTEGER PRIMARY KEY,
    order_id   INTEGER NOT NULL UNIQUE,   -- at most one review per order
    rating     INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment    TEXT,                      -- optional, may be NULL
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
