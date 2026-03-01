-- creates the table unique_id

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1i UNIQUE,
	name VARCHAR(256)
);
