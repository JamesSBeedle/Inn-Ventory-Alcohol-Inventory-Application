from db.run_sql import run_sql

from models.supplier import Supplier
from models.product import Product
import repositories.product_repository as product_repository


def save(supplier):
    sql = "INSERT INTO suppliers (name, address, phone_number, product) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [supplier.name, supplier.address, supplier.phone_number, supplier.product]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier