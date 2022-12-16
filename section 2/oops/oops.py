class Item:

    def __init__(self, name, price, quantity):            # magic methods -> when instance is created, python calls init method first in class.
        self.name = name       # dynamically assign attributes
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("parag", 100, 5)
item1.price = 5
item1.quantity = 100
#print(item1.calculate_total_price(item1.price, item1.quantity))

print(item1.name)                       # parag