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

        gcd = self.gcd(self.numerator,self.denominator)
        lowest_numerator = self.numerator // gcd
        return str(lowest_numerator)


    def get_denominator(self):
        gcd = self.gcd(self.numerator,self.denominator)
        lowest_denominator = self.denominator // gcd
        return str(lowest_denominator)

    def get_fraction(self):
        numerator = int(self.get_numerator())
        denominator = int(self.get_denominator())
        if denominator == 1:
            return str(numerator)
        if denominator < 0:
            numerator = numerator*-1
            denominator = denominator*-1
        return str(numerator) + "/" + str(denominator)
