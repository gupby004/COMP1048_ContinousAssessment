class Product:
    def __init__(self, id, name, description, price):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__price = round(value, 2)
        else:
            print("Must be positive")

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, value):
        if isinstance(value, int) and value >= 0:
            self.__quantity = value
        else:
            print("Quantity must be a non-negative integer.")

    def increase_quantity(self, amount):
        if isinstance(amount, int) and amount >=0:
            self.__quantity += amount
        else:
            print("the amount should be positive.")

    def decrease_quantity(self, amount):
        if isinstance(amount, int) and amount <= self.__quantity:
            self.__quantity -= amount
        else:
            print("the amount should be positive.")

    def __str__(self):
        return f"""Product: {self.__name} 
Description: {self.__description}
Quantity: {self.__quantity} 
Price: ${self.__price} each. """

    id = property(get_id)
    name = property(get_name)
    description = property(get_description)
    price = property(get_price, set_price)
    quantity = property(get_quantity, set_quantity)

class Store:
    def __init__(self, name, money):
        self.__name = name
        self.__money = money
        self.__products = []

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            print("Invalid")

    def get_money(self):
        return self.__money

    def set_money(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__money = value
        else:
            print("Money can't be negative.")

    def get_products(self):
        return self.__products

    def set_products(self, value):
        if isinstance(value, list):
            self.__products = value
        else:
            print("must be a list")

    def order_product(self, product, quantity):
        for p in self.__products:
            if p.id == product.id:
                p.increase_quantity(quantity)
                break
        else:
            product.set_quantity(quantity)
            self.__products.append(product)


    def sell_product(self, id, amount):
        product = self.find_product(id)
        if product:
            if product.quantity >= amount:
                product.decrease_quantity(amount)
                self.__money += amount * product.price
                if product.quantity == 0:
                    print(f"The item: {product.name} is sold out.")
            else:
                print(f"This quantity ({amount}) cannot be sold as there are only ({product.quantity}) {product.name}(s) remaining in stock.")
        else:
            print("Product not found.")

    def markup_prices(self, multiplier):
        if isinstance(multiplier, float) and multiplier > 0:
            for p in self.__products:
                p.price = p.price * multiplier

    def find_product(self, id):
        for product in self.__products:
            if product.id == id:
                return product
        return None

    def __str__(self):
        lines = [self.__name.upper(), f"Current Holdings: ${self.__money:.1f}"]
        if not self.__products:
            lines.append("This store is out of stock... of everything. *shrug*")
        else:
            lines.append("Current Stock:")
            for product in self.__products:
                lines.append("===========")
                lines.append(str(product))
                lines.append("===========")

        return "\n".join(lines)


    name = property(get_name, set_name)
    money = property(get_money, set_money)
    products = property(get_products, set_products)


store = Store("Sleep Token", 1000.0)
pillow = Product(1, "Pillow Set", "Set of two bamboo material pillows.", 45.99)
candle = Product(2, "Scented Candle", "Sandalwood, dual-wick candle.", 39.99)


store.order_product(pillow, 2)
store.order_product(candle, 4)
print(store)