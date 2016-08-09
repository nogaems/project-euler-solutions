from combinations import get_count
from fractions import Fraction

def get_numbers(N):
    """
    Returns a list of the Bernoulli numbers up to N inclusive.

    """
    N = int(N)
    B = [Fraction(0)] * (N+1)
    B[0] = Fraction(1)
    B[1] = Fraction(-1, 2)
    for n in xrange(2, N+1, 2):
        coef = Fraction(-1, n + 1)
        adder = Fraction(0)
        for k in xrange(1, n + 1):
            adder = adder + get_count(n + 1, k + 1) * B[n-k]
        B[n] = coef * adder
    return B
