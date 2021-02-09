from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", inventory = products, title="Inn-Ventory - Full Inventory")

@products_blueprint.route("/products/<id>", methods=["GET"])
def show_product(id):
    product = product_repository.select(id)
    return render_template("/products/show.html", product = product, title="Inn-Ventory - Product")

@products_blueprint.route("/products/new", methods=["GET"])
def new_product():
    suppliers = supplier_repository.select_all()
    return render_template("products/new.html", all_suppliers = suppliers, title="Inn-Ventory - Create Product")

@products_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form["name"]
    category = request.form["category"]
    in_stock = request.form["in_stock"]
    cost_price = request.form["cost_price"]
    sale_price = request.form["sale_price"] #change to be markup values in dropdown
    description = request.form["description"]
    minimum_stock_level = request.form["minimum_stock_level"]
    #set_markup function (cost_price, sale_price) sale_price=set_markup 
    supplier = supplier_repository.select(request.form['supplier_id'])
    product = Product(name, category, in_stock, cost_price, sale_price, description,minimum_stock_level, supplier)
    product_repository.save(product)
    return redirect("/products")

@products_blueprint.route("/products/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select(id)
    suppliers = supplier_repository.select_all()
    return render_template("products/edit.html", product = product, all_suppliers = suppliers, title="Inn-Ventory - Edit Product")

@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    category = request.form["category"]
    in_stock = request.form["in_stock"]
    cost_price = request.form["cost_price"]
    sale_price = request.form["sale_price"]
    description = request.form["description"]
    minimum_stock_level = request.form["minimum_stock_level"]
    supplier = supplier_repository.select(request.form['supplier_id'])
    product = Product(name, category, in_stock, cost_price, sale_price, description,minimum_stock_level, supplier, id)
    product_repository.update(product)
    return redirect("/products")
    

@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect ("/products")



   