CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    date_of_registration TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    username VARCHAR(100) NOT NULL UNIQUE,
);

CREATE TABLE IF NOT EXISTS Global_Equities(
    equity_id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(10) UNIQUE NOT NULL,
    equity_name VARCHAR(255) NOT NULL,
    type VARCHAR(20),
    current_price DECIMAL(12, 4),
    sector VARCHAR(100),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Personal_Portfolio(
    portfolio_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    equity_id INT NOT NULL,
    quantity DECIMAL(12, 4) NOT NULL,
    purchase_price DECIMAL(12, 4) NOT NULL,
    date_added DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (equity_id) REFERENCES Global_Equities(equity_id)
);