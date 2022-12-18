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

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("parag", 11, 10)          # AssertionError: Price -11 is not greater than or equal to zero!
item1.price = 5
item1.quantity = 100
print(item1.calculate_total_price())

print(Item.pay_rate)                     # 0.8 class attribute
print(item1.pay_rate)                    # 0.8 instance attribute

print(Item.__dict__)            # All the attributes for class level
# {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function Item.__init__ at 0x7ff5cca05ea0>, 'calculate_total_price': <function Item.calculate_total_price at 0x7ff5cca060e0>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
print(item1.__dict__)           # All the attributes for instance level
# {'name': 'parag', 'price': 5, 'quantity': 100}
