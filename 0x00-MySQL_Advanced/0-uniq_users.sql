-- create tabel users with some requerment

CREATE TABLE IF NOT EXISTS users(
	id SERIAL PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
