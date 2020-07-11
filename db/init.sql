CREATE DATABASE invoice_challenge;
use invoice_challenge;

-- Id: UUID,
-- Document: STRING,
-- Description: STRING,
-- Amount: CURRENCY,
-- ReferenceMonth: DATETIME,
-- ReferenceYear: INT,
-- CreatedAt: DATETIME,
-- IsActive: BOOL,
-- DeactiveAt: DATETIME
CREATE TABLE invoice (
  document VARCHAR(40),
  description VARCHAR(200)
);

INSERT INTO invoice
  (document, description)
VALUES
  ('MC-Donalds', 'fast food'),
  ('C&A', 'general store');