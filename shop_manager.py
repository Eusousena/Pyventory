class Products:
    # Products class than initializes name, price and stock.
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Method that adds products to stock
    def __add__(self, other):
        if isinstance(other, int):
            self.stock += other
            return self
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Product' and '{}'".format(type(other)))        

    # Method that sub products to stock
    def __sub__(self, other):
        if isinstance(other, int) and self.stock < 0:
            self.stock -= other
            return self
        else:
            raise TypeError("Unsupport operand type(s) for -: 'product' and '{}'".format(type(other)))


product1 = Products("Orange", 3.15, 4)
product2 = Products("Apple", 1.23, 5)

product1 += 2
print(product1.stock)

product2 -= 10
print(product2.stock)