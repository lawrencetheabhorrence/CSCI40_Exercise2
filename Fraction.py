class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        # TODO
        pass

    def gcd(a, b):
        # TODO
        pass

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, new_numerator):
        gcd = Fraction.gcd(new_numerator, self.denominator)
        self._numerator = new_numerator // gcd
        self._denominator //= gcd

    def get_numerator(self):
        # TODO
        pass

    def get_denominator(self):
        # TODO
        pass

    def get_fraction(self):
        # TODO
        pass

