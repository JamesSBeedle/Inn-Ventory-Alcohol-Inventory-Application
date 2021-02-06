DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;


CREATE TABLE suppliers ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_number INT,
    product VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    in_stock INT,
    cost_price FLOAT,
    sale_price FLOAT,
    description TEXT,
    supplier_id INT REFERENCES suppliers(id)
);