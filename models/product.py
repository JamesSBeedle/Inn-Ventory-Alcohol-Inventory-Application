class Product:

    def __init__(self, name, category, in_stock, cost_price, mark_up, sale_price, description,minimum_stock_level, supplier, id = None ):

        
    @classmethod
    def set_markup(cls, unit_price, percentage):
        sale_price = ((float(unit_price) / 100) * float(percentage)) + float(unit_price)
        return sale_price 

