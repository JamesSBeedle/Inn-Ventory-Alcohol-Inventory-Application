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

def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row["name"], row["address"], row["phone_number"], row["product"], row["id"])
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result["name"], result["address"], result["phone_number"], result["product"], result["id"])
    return supplier

def update(supplier):
    sql = "UPDATE suppliers SET (name, address, phone_number, product) = (%s, %s, %s, %s) Where id = %s"
    values = [supplier.name, supplier.address, supplier.phone_number, supplier.product, supplier.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

