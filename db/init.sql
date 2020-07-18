CREATE DATABASE invoice_challenge;
use invoice_challenge;

CREATE TABLE IF NOT EXISTS invoice (
  id BINARY(16) PRIMARY KEY,
  document VARCHAR(255),
  description VARCHAR(255),
  amount DECIMAL(19, 2),
  referenceMonth DATETIME,
  referenceYear INT,
  createdAt DATETIME NOT NULL DEFAULT NOW(),
  isActive BOOLEAN NOT NULL DEFAULT true,
  deactiveAt DATETIME
);

INSERT INTO invoice
  (id, document, description, amount, referenceMonth, referenceYear)
VALUES
  (UNHEX(REPLACE(UUID(), "-", "")), 'MC-Donalds', 'fast food', 100.24, NOW(), MONTH(NOW())),
  (UNHEX(REPLACE(UUID(), "-", "")), 'C&A', 'general store', 1000222333.99, NOW(), MONTH(NOW()));
