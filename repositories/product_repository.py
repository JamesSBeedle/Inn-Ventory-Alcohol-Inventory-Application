from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (name, category, in_stock, cost_price, sale_price, description, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.category, product.in_stock, product.cost_price, product.sale_price, product.description, product.supplier]
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
        product = Product(row["name"], row["category"], row["in_stock"], row["cost_price"], row["sale_price"], row["description"], supplier, row["id"])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = supplier_repository.select(result["supplier_id"])
        product = Product(result["name"], result["category"], result["in_stock"], result["cost_price"], result["sale_price"], result["description"], supplier, result["id"])
    return product

