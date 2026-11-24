
CREATE TABLE loyalty_accounts (
    account_id    INTEGER PRIMARY KEY,
    customer_id   INTEGER NOT NULL UNIQUE,
    date_created  TEXT NOT NULL,
    tier          TEXT NOT NULL DEFAULT 'bronze'
                  CHECK (tier IN ('bronze', 'silver', 'gold')),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE rewards (
    reward_id      INTEGER PRIMARY KEY,
    name           TEXT NOT NULL,
    points_cost    INTEGER NOT NULL,
    tier_required  TEXT NOT NULL
                   CHECK (tier_required IN ('bronze', 'silver', 'gold'))
);

-- Junction table: orders *:* rewards
CREATE TABLE reward_transactions (
    order_id     INTEGER,
    reward_id    INTEGER,
    points_cost  INTEGER NOT NULL,
    PRIMARY KEY (order_id, reward_id),
    FOREIGN KEY (order_id)  REFERENCES orders(order_id),
    FOREIGN KEY (reward_id) REFERENCES rewards(reward_id)
);
