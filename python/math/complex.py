'''
Description: Contains a simple implementation of complex numbers
'''
from decimal import Decimal as Dec


class Complex:
    i_unit = 'i'

    def __init__(self, a, b):
        self.mutate(a, b)

    def mutate(self, a, b):
        self.a = Dec(a)
        self.b = Dec(b)
        return self

    def add(self, other, mut=False):
        '''Complex Addition'''
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b) if not mut else self.mutate(a, b)

    def inv(self, mut=False):
        '''Complex Additive Inverse'''
        a, b = -self.a, -self.b
        return Complex(a, b) if not mut else self.mutate(a, b)

    def sub(self, other, mut=False):
        '''Complex Subtraction'''
        self.add(other.inv(), mut)

    def mul(self, other, mut=False):
        '''Complex Multiplication'''
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return Complex(a, b) if not mut else self.mutate(a, b)

    def conj(self, mut=False):
        '''Complex Conjugate'''
        a, b = self.a, self.b
        return Complex(a, -b) if not mut else self.mutate(a, -b)

    def div(self, other, mut=False):
        '''Complex Division'''
        dividend = self.mul(other.conj())
        divisor = other.mul(other.conj())
        a = dividend.a / divisor.a
        b = dividend.b / divisor.a
        return Complex(a, b) if not mut else self.mutate(a, b)

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return '0'
        a_part = self.a if self.a != 0 else ''
        b_part = f'+{self.b}{self.i_unit}' if self.b != 0 else ''
        return f'{a_part}{b_part}'
