class Item:

    def __init__(self):            # magic methods -> when instance is created, python calls init method first in class.
        print("I M CREATED.")

    def calculate_total_price(self, x, y):
        return x * y

item1 = Item()
item1.price = 5
item1.quantity = 100
#print(item1.calculate_total_price(item1.price, item1.quantity))

