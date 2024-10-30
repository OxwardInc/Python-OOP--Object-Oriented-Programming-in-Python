class Fraction:

    def __init__(self, numerator, denominator=1):

        self.nr = numerator

        self.dr = denominator

        if self.dr < 0:

            self.nr *= -1

            self.dr *= -1

        self._reduce()


    def show(self):

        print(f'{self.nr} / {self.dr}')

    def __str__(self):
        return f'{self.nr} / {self.dr}'
    
    def __repr__(self):
        return f'Fraction({self.nr}, {self.dr})'
    

    def __add__(self, other):

        if isinstance(other, int):

            other = Fraction(other)

        f = Fraction(self.nr * other.dr +  other.nr * self.dr)

        f._reduce()

        return f
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):

        if isinstance(other, int):

            other = Fraction(other)

        f = Fraction(self.nr * other.dr -  other.nr * self.dr)

        f._reduce()

        return f

    def __mul__(self, other):

        if isinstance(other, int):

            other = Fraction(other)

        f = Fraction(self.nr * other.nr,  other.dr * self.dr)

        f._reduce()

        return f

    def __eq__(self, other):
        return (self.nr * other.dr) == (self.dr * other.nr)
    
    def __lt__(self, other):
        return (self.nr * other.dr) < (self.dr * other.nr)

    def __le__(self, other):
        return (self.nr * other.dr) <= (self.dr * other.nr)


    def _reduce(self):
        if (Fraction.hcf(self.nr, self.dr)) == 0:

            return


        self.nr //= Fraction.hcf(self.nr, self.dr)

        self.dr //= Fraction.hcf(self.nr, self.dr)