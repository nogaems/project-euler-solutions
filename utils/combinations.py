from fractions import Fraction

def get_count(n, k):
    """
    Returns the number of permutations of n by k.

    """ 
    result = Fraction(1)
    n, k = int(n), int(k) 
    for i in range(1, k + 1):
        result *= Fraction(n + 1 - i, i)
    return int(result)
