DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    in_stock INT,
    cost_price INT,
    sale_price INT,
    description TEXT
);

CREATE TABLE suppliers ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_number INT,
    product_id INT REFERENCES products(id) ON DELETE CASCADE

)