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
        
    @classmethod
    def set_markup(cls, unit_price, percentage):
        sale_price = ((float(unit_price) / 100) * float(percentage)) + float(unit_price)
        return sale_price 
# to set the sale price for product you need to add a % markup

# so cost_price * %markup you want = markup amount
# you then add this to the cost_price to get the sale amount
#eg (cost_price * mark_up)+ cost_price = sale_price
