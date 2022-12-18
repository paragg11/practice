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

    def apply_discount(self):
        self.price = self.price * self.pay_rate   # NameError: name 'pay_rate' is not defined
                                                  # You cannot access by using pay_rate intead use Item.pay_rate


item1 = Item("parag", 11, 10)
item1.apply_discount()
print(item1.price)                  # 8.8

item2 = Item("p", 10, 10)
item2.pay_rate = 30
item2.apply_discount()
print(item2.price)



