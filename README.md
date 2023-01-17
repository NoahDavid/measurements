# A Library for Error Propagation

Written by Noah Koliadko

## Installation

Run this command to instal the latest version:

``` sh
$ pip install --upgrade git+https://github.com/NoahDavid/measurements
```

## Usage

The `Measurement` class is the main class of this library. It is used to represent a measurement with an uncertainty. It is initialized with a value and an uncertainty.

``` python
>>> from measurements import Measurement
>>> m = Measurement(1, 0.1)
>>> m
1.0 ± 0.1
```

The `Measurement` class has a number of methods for performing arithmetic operations. These methods return a new `Measurement` object with the correct value and an uncertainty that is calculated using the uncertainty propagation formula:

$\Delta z = \sqrt{\left(\frac{\partial z}{\partial x}\Delta x\right)^2 + \left(\frac{\partial z}{\partial y}\Delta y\right)^2}$

``` python
>>> m + 1
2.0 ± 0.1
>>> m - 1
0.0 ± 0.1
>>> m * 2
2.0 ± 0.2
>>> m / 2
0.50 ± 0.05
>>> 2 / m
2.00 ± 0.20
>>> m ** 2
1.0 ± 0.2
>>> 2 ** m
2.00 ± 0.20
>>> m ** 0.5
1.00 ± 0.05
```

This also works between two `Measurement` objects:

``` python
>>> m1 = Measurement(1, 0.1)
>>> m2 = Measurement(2, 0.2)
>>> m1 + m2
3.0 ± 0.2
>>> m1 - m2
-1.0 ± 0.2
>>> m1 * m2
2.0 ± 0.3
>>> m1 / m2
0.50 ± 0.07
>>> m1 ** m2
1.0 ± 0.2
```

The `Measurement` class also has a number of methods for performing trigonometric operations. These methods return a new `Measurement` object with the correct value and a calculated uncertainty.

``` python
>>> m = Measurement(0.5, 0.1)
>>> m.sin()
0.48 ± 0.09
>>> m.cos()
0.88 ± 0.05
>>> m.tan()
0.5 ± 0.1
>>> m.asin()
0.5 ± 0.1
>>> m.acos()
1.0 ± 0.1
>>> m.atan()
0.46 ± 0.08
>>> m = Measurement(1.5, 0.1)
>>> m.sinh()
2.1 ± 0.2
>>> m.cosh()
2.4 ± 0.2
>>> m.tanh()
0.91 ± 0.02
>>> m.asinh()
1.19 ± 0.06
>>> m.acosh()
0.96 ± 0.09
>>> m = Measurement(0.5, 0.1)
>>> m.atanh()
0.5 ± 0.1
```

The `Measurement` class also has a number of methods for some other operations. These methods return a new `Measurement` object with the correct value and a calculated uncertainty.

``` python
>>> m = Measurement(1, 0.1)
>>> m.exp()
2.7 ± 0.3
>>> m = Measurement(11, 0.2)
>>> m.log()
2.40 ± 0.02
>>> m.log10()
1.041 ± 0.008
>>> m = Measurement(9, 0.1)
>>> m.sqrt()
3.00 ± 0.02
>>> m = Measurement(-1, 0.1)
>>> m.abs()
1.0 ± 0.1
```

A `Measurement` object stores the value and uncertainty with untruncated precision `Decimal` objects. When printing a `Measurement` object, the value and uncertainty are truncated to the significant figures determined in the uncertainty by standard convention. If you call the method `round_unc()` on a `Measurement` object, the value and uncertainty will be rounded to the number of significant figures in the uncertainty.

``` python
>>> m = Measurement('1.23456789', '0.123456789')
>>> m
1.2 ± 0.1
>>> m.val
Decimal('1.23456789')
>>> m.unc
Decimal('0.123456789')
>>> m.round_unc()
>>> m
1.2 ± 0.1
>>> m.val
Decimal('1.2')
>>> m.unc
Decimal('0.1')
```

## License

None yet!