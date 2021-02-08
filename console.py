import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository.delete_all()
supplier_repository.delete_all()

supplier1 = Supplier("Timothy Taylors", "Knowle Spring Brewery, Keighley", "01535-555-555", "Landlord")
supplier_repository.save(supplier1)

supplier2 = Supplier("ABV Wholesale", "Dalton Lane, Keighley", "01535-699-699", "Budvar")
supplier_repository.save(supplier2)

supplier3 = Supplier("Premier Cru", "Ballpark Road, Shipley", "01274-545-667", "Chenin Blanc")
supplier_repository.save(supplier3)

supplier_repository.select_all()

product1 = Product("Landlord", "Draught", 12, 1.23, 3.00, "A Strong Pale Ale", supplier1)
product_repository.save(product1)

product2 = Product("Budvar", "Bottles", 24, 2.20, 4.50, "A Czech Pilsner", supplier2)
product_repository.save(product2)

product3 = Product("Chenin Blanc", "Wine", 12, 9.50, 16.50, "Crisp French White Wine", supplier3)
product_repository.save(product3)


pdb.set_trace()