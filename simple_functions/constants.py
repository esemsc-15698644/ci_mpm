from numpy import sqrt
from simple_functions.functions1 import factorial
import functools


__all__ = ['my_pi']


def my_pi(terms=1):
    return 1./(2.*sqrt(2.)/9801.*rsum(terms))


@functools.cache
def rsum(n):
    t = factorial(4*n)*(1103+26390*n)/(factorial(n)**4*396**(4*n))
    return t + rsum(n-1) if n else t
