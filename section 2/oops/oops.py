import csv

class Item:

    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):  # magic methods -> when instance is created, python calls init method \
        # first in class.

        # run validations to the received arguments

        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # assign to self object
        self.name = name                                  # dynamically assign attributes
        self.price = price
        self.quantity = quantity

        # actions to execute
        # Item.all.append(self)

        def __repr__(self):
            return f"Item '{self.name}' {self.price} {self.quantity}"

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(self):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)      # The DictReader class provides fieldnames attribute. \
            # It returns the dictionary keys used as header of file
            items = list(reader)

        for item in items:
            print(item)

    def apply_discount(self):
        self.price = self.price * self.pay_rate   # NameError: name 'pay_rate' is not defined
                                                  # You cannot access by using pay_rate intead use Item.pay_rate


Item.instantiate_from_csv()             # {'name': 'phone', ' price': ' 100', ' quantity': ' 1'}
                                        # {'name': 'laptop', ' price': ' 1000', ' quantity': ' 3'}
                                        # {'name': 'cable, 10, 5\nmouse"', ' price': ' 50', ' quantity': ' 5'}
                                        # {'name': 'keyboard', ' price': ' 75', ' quantity': ' 5'}


