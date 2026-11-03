#!/usr/bin/env python3
"""Represents a binomial distribution."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the distribution from data or given n and p."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - (variance / mean)
            self.n = round(mean / p)
            self.p = float(mean / self.n)

    def factorial(self, num):
        """Return the factorial of a non-negative integer num."""
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    def pmf(self, k):
        """Calculate the value of the PMF for k successes."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        comb = (self.factorial(self.n) /
                (self.factorial(k) * self.factorial(self.n - k)))
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculate the value of the CDF for k successes."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        total = 0
        for i in range(k + 1):
            total += self.pmf(i)
        return total
