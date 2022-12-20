import csv

class Item:                     # parent class
    pass

class Phone(Item):              # child class
    pass

phone1 = Phone()
phone1.broken_phone = 1
phone2 = Item()
phone2.broken_phone = 10