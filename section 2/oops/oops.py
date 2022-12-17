class Item:

    def __init__(self, name: str, price: float, quantity=0):  # magic methods -> when instance is created, python calls init method \
        # first in class.

        # run validations to the received arguments

        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # assign to self object
        self.name = name                                  # dynamically assign attributes
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("parag", -11, 10)          # AssertionError: Price -11 is not greater than or equal to zero!
item1.price = 5
item1.quantity = 100
print(item1.calculate_total_price())




