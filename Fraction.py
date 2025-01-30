class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("NO DIVIDING BY ZERO!!!")
        if not isinstance(denominator, int):
            raise ValueError("Denominator should be an integer")

        if isinstance(numerator, str):
            num, denom = numerator.split("/")
            self.numerator = int(num)
            self.denominator = int(denom)

        if isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError("Both inputs should be integers.")
        if a == 0 or b == 0:
            return 0
        if a < b:
            return Fraction.gcd(b, a)
        if a < 0 or b < 0:
            return Fraction.gcd(abs(a), abs(b))
        if a % b == 0:
            return b
        while a % b != 0:
            return Fraction.gcd(b, a % b)

    def get_numerator(self):
        # TODO
        pass

    def get_denominator(self):
        # TODO
        pass

    def get_fraction(self):
        # TODO
        pass
