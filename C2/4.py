# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.

import code

class flower:
    def __init__(self, flower, petals, price):
        self._flower = flower
        self._petals = petals
        self._price = price

    def get_flower(self):
        return self._flower

    def get_petals(self):
        return self._petals

    # Convert returned result from float to string
    # >> > print rose.get_price()
    # 20.99
    # >> > print type(rose.get_price())
    # < type
    # 'str' >
    # >> >

    def get_price(self):
        return str(self._price)

# Initiated with <rose.pluck_petal(rose._petals)>
    def pluck_petal(self, petals):
        self._petals -= 1
        print ('Remaining petals = %s' % petals)


def main():
    rose = flower('rose', 4, float(20.99))
    code.interact(local=locals())

main()