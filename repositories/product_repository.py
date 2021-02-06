from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

def save(product):
    sql = "INSERT INTO products (name, category, in_stock, cost_price, sale_price, description, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.category, product.in_stock, product.cost_price, product.sale_price, product.description, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product