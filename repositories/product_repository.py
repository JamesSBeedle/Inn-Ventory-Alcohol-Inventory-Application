from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (name, category, in_stock, cost_price, mark_up, sale_price, description, minimum_stock_level, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.category, product.in_stock, product.cost_price, product.mark_up, product.sale_price, product.description, product.minimum_stock_level, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        supplier = supplier_repository.select(row["supplier_id"])
        product = Product(row["name"], row["category"], row["in_stock"], row["cost_price"],row["mark_up"], row["sale_price"], row["description"], row["minimum_stock_level"], supplier, row["id"])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = supplier_repository.select(result["supplier_id"])
        product = Product(result["name"], result["category"], result["in_stock"], result["cost_price"],result["mark_up"], result["sale_price"], result["description"], result["minimum_stock_level"], supplier, result["id"])
    return product

def update(product):
    sql = "UPDATE products SET (name, category, in_stock, cost_price, mark_up, sale_price, description,minimum_stock_level, supplier_id) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.category, product.in_stock, product.cost_price, product.mark_up, product.sale_price, product.description, product.minimum_stock_level, product.supplier.id, product.id]
    run_sql(sql, values)
   
def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

