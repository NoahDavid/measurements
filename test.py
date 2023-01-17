from measurements import Measurement as M

# Run tests on all the parts of the Measurement class

# Test the constructor
assert M(1, 0.1) == M(1, 0.1)
assert M(1, 0.1) != M(1, 0.2)
assert M(1, 0.1) != M(2, 0.1)
assert M(1, 0.1) != M(2, 0.2)


# Test the __str__ method with pretty printing
print(f'1 ± 0.1 = {M(1, 0.1)}')

# Test the __repr__ method with pretty printing
print(f'1 ± 0.1 = {repr(M(1, 0.1))}')

# Test the __add__ method with pretty printing
print(f'1 ± 0.1 + 1 ± 0.1 = {M(1, 0.1) + M(1, 0.1)}')

# Test the __sub__ method with pretty printing
print(f'1 ± 0.1 - 1 ± 0.1 = {M(1, 0.1) - M(1, 0.1)}')

# Test the __mul__ method with pretty printing
print(f'1 ± 0.1 * 1 ± 0.1 = {M(1, 0.1) * M(1, 0.1)}')

# Test the __truediv__ method with pretty printing
print(f'1 ± 0.1 / 1 ± 0.1 = {M(1, 0.1) / M(1, 0.1)}')

# Test the __pow__ method with pretty printing
print(f'1 ± 0.1 ** 1 ± 0.1 = {M(1, 0.1) ** M(1, 0.1)}')

# Test the __radd__ method with pretty printing
print(f'1 + 1 ± 0.1 = {1 + M(1, 0.1)}')

# Test the __rsub__ method with pretty printing
print(f'1 - 1 ± 0.1 = {1 - M(1, 0.1)}')

# Test the __rmul__ method with pretty printing
print(f'1 * 1 ± 0.1 = {1 * M(1, 0.1)}')

# Test the __rtruediv__ method with pretty printing
print(f'1 / 1 ± 0.1 = {1 / M(1, 0.1)}')

# Test the __rpow__ method with pretty printing
print(f'1 ** 1 ± 0.1 = {1 ** M(1, 0.1)}')

# Test the cos method with pretty printing
print(f'cos(1 ± 0.1) = {M(1, 0.1).cos()}')

# Test the sin method with pretty printing
print(f'sin(1 ± 0.1) = {M(1, 0.1).sin()}')

# Test the tan method with pretty printing
print(f'tan(1 ± 0.1) = {M(1, 0.1).tan()}')

# Test the acos method with pretty printing
print(f'acos(0.5 ± 0.1) = {M(0.5, 0.1).acos()}')

# Test the asin method with pretty printing
print(f'asin(0.5 ± 0.1) = {M(0.5, 0.1).asin()}')

# Test the atan method with pretty printing
print(f'atan(0.5 ± 0.1) = {M(0.5, 0.1).atan()}')

# Test the atan2 method with pretty printing
print(f'atan2(0.5 ± 0.1, 1 ± 0.1) = {M(0.5, 0.1).atan2(M(1, 0.1))}')

# Test the cosh method with pretty printing
print(f'cosh(1 ± 0.1) = {M(1, 0.1).cosh()}')

# Test the sinh method with pretty printing
print(f'sinh(1 ± 0.1) = {M(1, 0.1).sinh()}')

# Test the tanh method with pretty printing
print(f'tanh(1 ± 0.1) = {M(1, 0.1).tanh()}')

# Test the acosh method with pretty printing
print(f'acosh(1.5 ± 0.1) = {M(1.5, 0.1).acosh()}')

# Test the asinh method with pretty printing
print(f'asinh(0.5 ± 0.1) = {M(0.5, 0.1).asinh()}')

# Test the atanh method with pretty printing
print(f'atanh(0.5 ± 0.1) = {M(0.5, 0.1).atanh()}')

# Test the exp method with pretty printing
print(f'exp(1 ± 0.1) = {M(1, 0.1).exp()}')

# Test the log method with pretty printing
print(f'log(1 ± 0.1) = {M(1, 0.1).log()}')

# Test the log10 method with pretty printing
print(f'log10(1 ± 0.1) = {M(1, 0.1).log10()}')

# Test the sqrt method with pretty printing
print(f'sqrt(1 ± 0.1) = {M(1, 0.1).sqrt()}')

# Test the abs method with pretty printing
print(f'abs(-1 ± 0.1) = {M(-1, 0.1).abs()}')