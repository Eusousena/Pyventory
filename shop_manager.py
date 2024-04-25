import cmd

class Products:
    # Products class than initializes name, price and stock.
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.log = []

    # Method that adds products to stock
    def __add__(self, other):
        if isinstance(other, int):
            self.stock += other
            self.log.append(f"Append {other} from stock")
            return self.stock
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Product' and '{}'".format(type(other)))        

    # Method that sub products to stock
    def __sub__(self, other):
        # Analicty if stock is int and protect para que não fique negative
        if isinstance(other, int) and self.stock - other < 0:
            self.stock -= other
            self.log.append(f"Subtraido {other} from stock")
            return self
        else:
            raise TypeError("Unsupport operand type(s) for -: 'product' and '{}'".format(type(other)))   
    
    # Show details of products
    def show(self):
        return self.name, self.price, self.stock, self.category

    # Update price of products
    def update_price(self, new_price):
        old_price = self.price
        self.price = new_price
        self.log.append(f"Price updated from {old_price} to {new_price}.")
        return f"Old price = {old_price}$\nprice actualiady = {new_price}$"
    
    # Update category of products
    def update_category(self, new_category):
        old_category = self.category
        self.category = new_category
        self.log.append(f"Category updated from {old_category} to {new_category}.")
        return f"Old category = {old_category}\ncategory actualiady = {new_category}"
    
    # Append discount in product
    def discount(self, value_discount):
        price_original = self.price
        self.price = price_original * (price_original + value_discount/100)
        return f'SALE!!! {self.name} went from {price_original}$ to {self.price}$'

    # Check if a stock of the products
    def check_stock(self):
        return self.stock    
    
    # Show transaction log
    def show_log(self):
        return self.log

    # Save transaction log to file
    def save_log(self, filename):
        with open(filename, 'w') as f:
            for entry in self.log:
                f.write(entry + '\n')


class StoreInterface(cmd.Cmd):
    intro = 'Bem-vindo à loja! Digite help ou ? para listar os comandos.\n'
    prompt = '(Shop) '

    def __init__(self):
        super().__init__()
        self.products = []

    def do_add_product(self, arg):
        'Adiciona um produto: NAME PRICE STOCK CATEGORY'
        name, price, stock, category = arg.split()
        self.products.append(Products(name, float(price), int(stock), category))

    def do_show_products(self, arg):
        'Mostra todos os produtos'
        for product in self.products:
            print(product.show())

    def do_exit(self, arg):
        'Sai da loja: EXIT'
        print('Obrigado por visitar a loja!')
        return True

if __name__ == '__main__':
    StoreInterface().cmdloop()



