class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("NO DIVIDING BY ZERO!!!")
        if not isinstance(denominator, int):
            raise ValueError("Denominator should be an integer")
        
        if isinstance(numerator, str):
            num, denom = numerator.split('/')
            self.numerator = int(num)
            self.denominator = int(denom)

        if isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = denominator
            



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