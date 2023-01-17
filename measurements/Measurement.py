import numpy as np
from decimal import Decimal, DecimalTuple

class Measurement:
    def __init__(self, val, unc):
        self.val = val
        self.unc = unc

    def in_range(self, num):
        return self.val + self.unc > num and self.val + self.unc < num

    def error_bar_widths(self, num):
        return abs(num - self.val) / self.unc

    def _round_result(self, obj):
        if type(obj.val) == Decimal and type(obj.unc) == Decimal:
            # We can round:
            a = obj.unc.as_tuple()
            a = DecimalTuple(a.sign, (a.digits[0], ), a.exponent + len(a.digits) - 1)
            unc = Decimal(a)
            val = round(obj.val, -1 * unc.as_tuple().exponent)
            return Measurement(val, unc)
        else:
            return obj

    def __mul__(self, other):
        if type(other) == Measurement:
            val = other.val * self.val
            unc = np.sqrt((other.unc * self.val)**2 + (self.unc * other.val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(other * self.val, other * self.unc)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if type(other) == Measurement:
            val = self.val / other.val
            unc = np.sqrt((other.unc * self.val / (other.val**2))**2 + (self.unc / other.val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(self.val / other, self.unc / other)
    
    def __add__(self, other):
        if type(other) == Measurement:
            unc = np.sqrt(other.unc**2 + self.unc**2)

            return Measurement(other.val + self.val, unc)
        else:
            return Measurement(self.val + other, self.unc)
    
    def __sub__(self, other):
        if type(other) == Measurement:
            unc = np.sqrt(other.unc**2 + self.unc**2)

            return Measurement(self.val - other.val, unc)
        else:
            return Measurement(self.val - other, self.unc)
    
    def  __str__(self):
        a = self._round_result(self)
        return f'{a.val} ± {a.unc}'
    
    def __repr__(self):
        return self.__str__()