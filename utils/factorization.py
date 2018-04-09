from .soe2 import get_primes
from math import sqrt, ceil


def get_max_factor(target):
    target = int(target)
    search = 1
    top_border = int(ceil(sqrt(target)))
    primes = get_primes(top_border)
    for n in primes:
        while True:
            if target % n == 0:
                target = target / n
                search = n
            else:
                break

    return target if search == 1 else search


def get_factor_list(target, primes=None, dump_path='', separator=' '):
    output = open(dump_path, 'w') if dump_path else None
    search = []
    top_border = int(ceil(target))
    if not primes:
        primes = get_primes(top_border)
    for n in primes:
        while True:
            if target % n == 0:
                target = target / n
                output.write(
                    str(n) + separator) if output else search.append(n)
            else:
                break
    return True if output else search
