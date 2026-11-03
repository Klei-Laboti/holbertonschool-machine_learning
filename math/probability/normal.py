#!/usr/bin/env python3
"""Represents a normal distribution."""


class Normal:
    """Represents a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize the distribution from data or given mean/stddev."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculate the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score."""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculate the value of the PDF for a given x-value."""
        pi = 3.1415926536
        e = 2.7182818285
        coefficient = 1 / (self.stddev * ((2 * pi) ** 0.5))
        exponent = -((x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        return coefficient * (e ** exponent)

    def erf(self, x):
        """Approximate the error function using a Taylor series."""
        pi = 3.1415926536
        coefficient = 2 / (pi ** 0.5)
        series = (x - (x ** 3) / 3 + (x ** 5) / 10 -
                  (x ** 7) / 42 + (x ** 9) / 216)
        return coefficient * series

    def cdf(self, x):
        """Calculate the value of the CDF for a given x-value."""
        arg = (x - self.mean) / (self.stddev * (2 ** 0.5))
        return 0.5 * (1 + self.erf(arg))
