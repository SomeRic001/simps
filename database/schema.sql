CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    date_of_registration TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    username VARCHAR(100) NOT NULL UNIQUE
);

-- increase the length for strings
CREATE TABLE IF NOT EXISTS Global_Equities(
    equity_id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(30) UNIQUE NOT NULL,
    equity_name VARCHAR(255) NOT NULL,
    type VARCHAR(255),
    current_price DECIMAL(12, 4),
    sector VARCHAR(255),
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

CREATE TABLE IF NOT EXISTS Equity_Price_History (
    price_id INT PRIMARY KEY AUTO_INCREMENT,
    equity_id INT NOT NULL,
    price DECIMAL(12, 4) NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (equity_id) REFERENCES Global_Equities(equity_id)
);

-- Income, Expenses and Savings tables for exploration page

CREATE TABLE IF NOT EXISTS Income (
    income_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER,
    month INTEGER,
    year INTEGER,
    amount DECIMAL(15, 2),
    source VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS Expenses (
    expense_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER,
    month INTEGER,
    year INTEGER,
    amount DECIMAL(15, 2),
    category VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS Savings (
    savings_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER,
    month INTEGER,
    year INTEGER,
    total_income DECIMAL(15, 2),
    total_expenses DECIMAL(15, 2),
    savings_amount DECIMAL(15, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);