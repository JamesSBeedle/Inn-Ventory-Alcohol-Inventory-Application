class Product:

    def __init__(self, name, category, in_stock, cost_price, mark_up, sale_price, description,minimum_stock_level, supplier, id = None ):
        self.name = name
        self.category = category
        self.in_stock = in_stock
        self.cost_price = cost_price
        self.mark_up = mark_up
        self.sale_price = sale_price
        self.description = description
        self.minimum_stock_level = minimum_stock_level
        self.supplier = supplier
        self.id = id


    #use a markup % and the cost price to calculate the sale price of a product.
    #use the calculation (cost price * 70%) + cost price = sale price
    #use the cost price and the markup given by the user input in add new product/ edit product
    #show the sale price calculated on the inventory page for the product.
        
    @classmethod
    def set_markup(cls, unit_price, percentage):
        sale_price = ((float(unit_price) / 100) * float(percentage)) + float(unit_price)
        return sale_price 

