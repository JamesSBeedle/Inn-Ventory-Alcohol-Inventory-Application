class Product:

    def __init__(self, name, category, in_stock, cost_price, sale_price, description,minimum_stock_level, supplier, id = None ):
        self.name = name
        self.category = category
        self.in_stock = in_stock
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.description = description
        self.minimum_stock_level = minimum_stock_level
        self.supplier = supplier
        self.id = id
        

    # def set_markup(self, cost_price, mark_up):
    #       markup_value = cost_price * mark_up
    #       sale_price = cost_price + markup_value
    #       return sale_price

# to set the sale price for product you need to add a % markup

# so cost_price * %markup wou want = markup amount
# you then add this to the cost_price to get the sale amount
#eg (cost_price * mark_up)+ cost_price = sale_price
