"""
Like the factory pattern this is also used to ease creation/modification of classes
without causing development pains.

There is a slight difference between Factory and Abstract Factory - 
Factory is used to create one type of implementation, like Fruits so it can create
only Apple, Orange, Mango etc
Abstract Factory is provides a factory to create factory for various types, like it can be
books, fruits, etc. Basically what you create is factory that does not need to know the type
of objects it is going to create (https://stackoverflow.com/a/1001803/6111200)
"""

class TheBrothersKaramazov:


    def __init__(self, price=1000):
        self.price = price


    def __str__(self):
        return "The Brothers Karamazov"


class CrimeAndPunishment:


    def __init__(self, price=500):
        self.price = price


    def __str__(self):
        return "Crime And Punishment"


class TheIdiot:


    def __init__(self, price=600):
        self.price = price


    def __str__(self):
        return "The Idiot"


class ItemAbstractFactory():

    
    def __init__(self, abstract_factory=None):
        self.abstract_factory = abstract_factory


    def show_item(self):
        obj = self.abstract_factory()

        print(f"Name of item - {obj}")
        print(f"Price of item - {obj.price}")


if __name__ == '__main__':
    item1 = ItemAbstractFactory(TheBrothersKaramazov)
    item2 = ItemAbstractFactory(CrimeAndPunishment)
    item3 = ItemAbstractFactory(TheIdiot)

    item1.show_item()
    item2.show_item()
    item3.show_item()