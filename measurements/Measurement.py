import math
from decimal import Decimal, DecimalTuple

class Measurement:
    def __init__(self, val, unc):
        if type(val) == Decimal and type(unc) == Decimal:
            self.val = val
            self.unc = unc
        else:
            self.val = Decimal(val)
            self.unc = Decimal(unc)

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
            unc = round(obj.unc, -1 * unc.as_tuple().exponent)
            return Measurement(val, unc)
        else:
            return obj

    def __mul__(self, other):
        if type(other) == Measurement:
            val = other.val * self.val
            unc = math.sqrt((other.unc * self.val)**2 + (self.unc * other.val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(Decimal(other) * self.val, Decimal(other) * self.unc)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if type(other) == Measurement:
            val = self.val / other.val
            unc = math.sqrt((other.unc * self.val / (other.val**2))**2 + (self.unc / other.val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(self.val / Decimal(other), self.unc / Decimal(other))
    
    def __add__(self, other):
        if type(other) == Measurement:
            unc = math.sqrt(other.unc**2 + self.unc**2)

            return Measurement(other.val + self.val, unc)
        else:
            return Measurement(self.val + Decimal(other), self.unc)
    
    def __sub__(self, other):
        if type(other) == Measurement:
            unc = math.sqrt(other.unc**2 + self.unc**2)

            return Measurement(self.val - other.val, unc)
        else:
            return Measurement(self.val - Decimal(other), self.unc)
    
    def __pow__(self, other):
        if type(other) == Measurement:
            val = self.val**other.val
            unc = math.sqrt((other.unc * Decimal(math.log(self.val)) * val)**2 + (self.unc * other.val / self.val * val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(self.val**Decimal(other), self.unc * Decimal(other) / self.val * self.val**Decimal(other))
    
    def __rpow__(self, other):
        if type(other) == Measurement:
            val = other.val**self.val
            unc = math.sqrt((other.unc * Decimal(math.log(self.val)) * val)**2 + (self.unc * other.val / self.val * val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(Decimal(other)**self.val, self.unc * Decimal(other) / self.val * Decimal(other)**self.val)
    
    def __eq__(self, other):
        if type(other) == Measurement:
            return self.val == other.val and self.unc == other.unc
        else:
            return self.val == Decimal(other) and self.unc == Decimal(0)
    
    def __ne__(self, other):
        if type(other) == Measurement:
            return self.val != other.val or self.unc != other.unc
        else:
            return self.val != Decimal(other) or self.unc != Decimal(0)

    def __lt__(self, other):
        if type(other) == Measurement:
            return self.val < other.val
        else:
            return self.val < Decimal(other)
    
    def __le__(self, other):
        if type(other) == Measurement:
            return self.val <= other.val
        else:
            return self.val <= Decimal(other)
    
    def __gt__(self, other):
        if type(other) == Measurement:
            return self.val > other.val
        else:
            return self.val > Decimal(other)
    
    def __ge__(self, other):
        if type(other) == Measurement:
            return self.val >= other.val
        else:
            return self.val >= Decimal(other)
    
    def cos(self):
        return Measurement(math.cos(self.val), self.unc * math.sin(self.val))
    
    def sin(self):
        return Measurement(math.sin(self.val), self.unc * math.cos(self.val))
    
    def tan(self):
        return Measurement(math.tan(self.val), self.unc / math.cos(self.val)**2)
    
    def acos(self):
        return Measurement(math.acos(self.val), self.unc / math.sqrt(1 - self.val**2))
    
    def asin(self):
        return Measurement(math.asin(self.val), self.unc / math.sqrt(1 - self.val**2))
    
    def atan(self):
        return Measurement(math.atan(self.val), self.unc / (1 + self.val**2))
    
    def cosh(self):
        return Measurement(math.cosh(self.val), self.unc * math.sinh(self.val))
    
    def sinh(self):
        return Measurement(math.sinh(self.val), self.unc * math.cosh(self.val))
    
    def tanh(self):
        return Measurement(math.tanh(self.val), self.unc / math.cosh(self.val)**2)
    
    def acosh(self):
        return Measurement(math.acosh(self.val), self.unc / math.sqrt(self.val**2 - 1))

    def asinh(self):
        return Measurement(math.asinh(self.val), self.unc / math.sqrt(self.val**2 + 1))

    def atanh(self):
        return Measurement(math.atanh(self.val), self.unc / (1 - self.val**2))

    def exp(self):
        return Measurement(math.exp(self.val), self.unc * math.exp(self.val))

    def log(self):
        return Measurement(math.log(self.val), self.unc / self.val)

    def sqrt(self):
        return Measurement(math.sqrt(self.val), self.unc / (2 * math.sqrt(self.val)))
    
    def  __str__(self):
        a = self._round_result(self)
        return f'{a.val} ± {a.unc}'
    
    def __repr__(self):
        return self.__str__()