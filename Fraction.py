class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator should not be zero.")

        # initial values of fraction just to avoid errors
        # with setters
        self._numerator = 0
        self._denominator = 1

        if isinstance(numerator, str):
            numbers = numerator.split("/")
            if len(numbers) > 0 and len(numbers) <= 2:
                try:
                    self.numerator = int(numbers[0])
                    # denominator is passed
                    if len(numbers) == 2:
                        self.denominator = int(numbers[1])
                except ValueError:
                    print("Invalid string passed, fraction will be set to 0")

        if isinstance(numerator, int) and isinstance(denominator, int):
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
        while (rem := a % b) > 0:
            a = b
            b = rem
        return b

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, new_numerator):
        gcd = Fraction.gcd(new_numerator, self.denominator)
        self._numerator = new_numerator // gcd
        self._denominator //= gcd

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, new_denominator):
        gcd = Fraction.gcd(new_denominator, self.numerator)
        self._denominator = new_denominator // gcd
        self._numerator //= gcd

    def get_numerator(self):

        gcd = self.gcd(self.numerator, self.denominator)
        lowest_numerator = self.numerator // gcd
        return str(lowest_numerator)

    def get_denominator(self):
        gcd = self.gcd(self.numerator, self.denominator)
        lowest_denominator = self.denominator // gcd
        return str(lowest_denominator)

    def get_fraction(self):
        numerator = int(self.get_numerator())
        denominator = int(self.get_denominator())
        if denominator == 1:
            return str(numerator)
        if denominator < 0:
            numerator = numerator * -1
            denominator = denominator * -1
        return str(numerator) + "/" + str(denominator)
