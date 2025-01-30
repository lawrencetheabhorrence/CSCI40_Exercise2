class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("NO DIVIDING BY ZERO!!!")
        if not isinstance(denominator, int):
            raise ValueError("Denominator should be an integer")

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass