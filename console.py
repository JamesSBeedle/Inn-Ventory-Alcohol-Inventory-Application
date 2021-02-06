import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

supplier1 = Supplier("Timothy Taylors", "Knowle Spring Brewery, Keighley", 669669, "Landlord")
supplier_repository.save(supplier1)

product1 = Product("Landlord", "Draught", 12, 1.23, 3.00, "A Strong Pale Ale", supplier1)
product_repository.save(product1)











pdb.set_trace()