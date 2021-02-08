from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository


suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)

@suppliers_blueprint.route("/suppliers/<id>", methods=["GET"])
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template("/suppliers/show.html", supplier = supplier)

@suppliers_blueprint.route("/suppliers/new", methods=["GET"])
def new_supplier():
    return render_template("suppliers/new.html")

@suppliers_blueprint.route("/suppliers", methods=["POST"])
def create_supplier():
    name = request.form['name']
    address = request.form['address']
    phone_number = request.form['phone_number']
    product = request.form['product']
    supplier = Supplier(name, address, phone_number, product)
    supplier_repository.save(supplier)
    print("SYHHKJTLKTLTLY", supplier)
    return redirect('/suppliers')

@suppliers_blueprint.route("/suppliers/<id>/edit", methods=["GET"])
def edit_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template("suppliers/edit.html", supplier = supplier)

@suppliers_blueprint.route("/suppliers/<id>", methods=["POST"])
def update_supplier(id):
    name = request.form["name"]
    address = request.form["address"]
    phone_number = request.form["phone_number"]
    product = request.form["product"]
    supplier = Supplier(name, address, phone_number, product, id)
    supplier_repository.update(supplier)
    return redirect("/suppliers")

@suppliers_blueprint.route("/suppliers/<id>/delete", methods=["POST"])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect("/suppliers")
