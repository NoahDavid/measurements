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
    
    ############################# Printing #############################
    
    def  __str__(self, sigfigs=2):
        a = self._round_result(self, sigfigs = sigfigs)
        return f'{a.val} ± {a.unc}'
    
    def __repr__(self, sigfigs=2):
        return self.__str__(sigfigs = sigfigs)

    def _round_result(self, obj, sigfigs=2):
        if type(obj.val) == Decimal and type(obj.unc) == Decimal:
            # We can round:
            a = obj.unc.as_tuple()
            a = DecimalTuple(a.sign, a.digits[0:sigfigs], a.exponent + len(a.digits) - sigfigs)
            unc = Decimal(a)
            val = round(obj.val, -1 * unc.as_tuple().exponent)
            unc = round(obj.unc, -1 * unc.as_tuple().exponent)
            return Measurement(val, unc)
        else:
            return obj
    
    def round_unc(self, sigfigs=2):
        rounded = self._round_result(self, sigfigs = sigfigs)
        self.unc = rounded.unc
        self.val = rounded.val

    ############################# Analysis #############################

    def within(self, other):
        if type(other) == Measurement:
            return abs(self.val - other.val) < self.unc + other.unc
        else:
            return abs(self.val - Decimal(other)) < self.unc

    ############################# Arithmetic #############################

    ### Multiplication ###

    # z = x * y
    # dz = sqrt((dx * y)**2 + (x * dy)**2)
    def __mul__(self, other):
        if type(other) == Measurement:
            val = other.val * self.val
            unc = math.sqrt((other.unc * self.val)**2 + (self.unc * other.val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(Decimal(other) * self.val, Decimal(other) * self.unc)

    def __rmul__(self, other):
        return self.__mul__(other)

    ### Division ###
    
    # z = x / y
    # dz = sqrt((dx / y)**2 + (x * dy / y**2)**2)
    def __truediv__(self, other):
        if type(other) == Measurement:
            val = self.val / other.val
            unc = math.sqrt((other.unc * self.val / (other.val**2))**2 + (self.unc / other.val)**2)

            return Measurement(val, unc)
        else:
            return Measurement(self.val / Decimal(other), self.unc / Decimal(other))
    
    def __rtruediv__(self, other):
        if type(other) == Measurement:
            val = other.val / self.val
            unc = math.sqrt((other.unc / self.val)**2 + (self.unc * other.val / (self.val**2))**2)

            return Measurement(val, unc)
        else:
            return Measurement(other, '0').__truediv__(self)

    ### Addition ###

    # z = x + y
    # dz = sqrt(dx**2 + dy**2)
    def __add__(self, other):
        if type(other) == Measurement:
            unc = math.sqrt(other.unc**2 + self.unc**2)

            return Measurement(other.val + self.val, unc)
        else:
            return Measurement(self.val + Decimal(other), self.unc)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    ### Subtraction ###

    # z = x - y
    # dz = sqrt(dx**2 + dy**2)
    def __sub__(self, other):
        if type(other) == Measurement:
            unc = math.sqrt(other.unc**2 + self.unc**2)

            return Measurement(self.val - other.val, unc)
        else:
            return Measurement(self.val - Decimal(other), self.unc)
    
    def __rsub__(self, other):
        if type(other) == Measurement:
            unc = math.sqrt(other.unc**2 + self.unc**2)

            return Measurement(other.val - self.val, unc)
        else:
            return Measurement(Decimal(other) - self.val, self.unc)
    
    ### Exponentiation ###

    # z = x**y
    # dz = sqrt((dy * ln(x) * z)**2 + (dx * y / x * z)**2)
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
    
    ############################# Math functions #############################

    ### Trigonometric functions ###
    # sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, and atanh are included.

    # z = cos(x)
    # dz = abs(-sin(x) * dx)
    def cos(self):
        return Measurement(math.cos(self.val), abs(float(self.unc) * math.sin(self.val)))
    
    # z = sin(x)
    # dz = abs(cos(x) * dx)
    def sin(self):
        return Measurement(math.sin(self.val), abs(float(self.unc) * math.cos(self.val)))
    
    # z = tan(x)
    # dz = abs((1 + tan(x)**2) * dx)
    def tan(self):
        return Measurement(math.tan(self.val), abs(float(self.unc) / math.cos(self.val)**2))

    # z = acos(x)
    # dz = abs(-1 / sqrt(1 - x**2) * dx)
    def acos(self):
        return Measurement(math.acos(self.val), abs(float(self.unc) / math.sqrt(1 - self.val**2)))
    
    # z = asin(x)
    # dz = abs(1 / sqrt(1 - x**2) * dx)
    def asin(self):
        return Measurement(math.asin(self.val), abs(float(self.unc) / math.sqrt(1 - self.val**2)))

    # z = atan(x)
    # dz = abs(1 / (1 + x**2) * dx)
    def atan(self):
        return Measurement(math.atan(self.val), abs(self.unc / (1 + self.val**2)))
    
    # z = atan2(y, x)
    # dz = abs(1 / (x**2 + y**2) * dx)
    def atan2(self, other):
        if type(other) == Measurement:
            val = math.atan2(self.val, other.val)
            unc = math.sqrt((self.unc / (self.val**2 + other.val**2))**2 + (other.unc / (self.val**2 + other.val**2))**2)

            return Measurement(val, unc)
        else:
            return Measurement(math.atan2(self.val, Decimal(other)), self.unc / (self.val**2 + Decimal(other)**2))

    # z = cosh(x)
    # dz = abs(sinh(x) * dx)
    def cosh(self):
        return Measurement(math.cosh(self.val), abs(float(self.unc) * math.sinh(self.val)))

    # z = sinh(x)
    # dz = abs(cosh(x) * dx)
    def sinh(self):
        return Measurement(math.sinh(self.val), abs(float(self.unc) * math.cosh(self.val)))

    # z = tanh(x)
    # dz = abs((1 - tanh(x)**2) * dx)
    def tanh(self):
        return Measurement(math.tanh(self.val), abs(float(self.unc) / math.cosh(self.val)**2))

    # z = acosh(x)
    # dz = abs(1 / sqrt(x**2 - 1) * dx)
    def acosh(self):
        return Measurement(math.acosh(self.val), abs(float(self.unc) / math.sqrt(self.val**2 - 1)))

    # z = asinh(x)
    # dz = abs(1 / sqrt(x**2 + 1) * dx)
    def asinh(self):
        return Measurement(math.asinh(self.val), abs(float(self.unc) / math.sqrt(self.val**2 + 1)))

    # z = atanh(x)
    # dz = abs(1 / (1 - x**2) * dx)
    def atanh(self):
        return Measurement(math.atanh(self.val), abs(self.unc / (1 - self.val**2)))

    ### Other functions ###
    # exp, log, log10, sqrt, and abs are included.

    # z = exp(x)
    # dz = abs(exp(x) * dx)
    def exp(self):
        return Measurement(math.exp(self.val), abs(float(self.unc) * math.exp(self.val)))

    # z = log(x)
    # dz = abs(1 / x * dx)
    def log(self):
        return Measurement(math.log(self.val), abs(self.unc / self.val))

    # z = log10(x)
    # dz = abs(1 / (x * log(10)) * dx)
    def log10(self):
        return Measurement(math.log10(self.val), abs(float(self.unc) / (float(self.val) * math.log(10))))

    # z = sqrt(x)
    # dz = abs(1 / (2 * sqrt(x)) * dx)
    def sqrt(self):
        return Measurement(math.sqrt(self.val), abs(float(self.unc) / (2 * math.sqrt(self.val))))

    # z = abs(x)
    # dz = abs(dx)
    def abs(self):
        return Measurement(abs(self.val), self.unc)
    
    ############################# Comparison Operators #############################

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