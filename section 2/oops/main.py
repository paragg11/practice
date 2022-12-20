import csv


class Item:                     # parent class
    def __init__(self, name):
            self.name = name


class Phone(Item):              # child class
    def __init__(self, name, broken_phone=100):
        # super function gives full access to attributes/methods of parent class.
        super().__init__(name)


phone1 = Phone("a")
