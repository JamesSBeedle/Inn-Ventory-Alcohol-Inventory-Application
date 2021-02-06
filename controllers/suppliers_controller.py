from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.supplier import Supplier
import supplier_repository as supplier_repository
import product_repository as product_repository


suppliers_blueprint = Blueprint("suppliers", __name__)