from soe2 import get_primes
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
    
    return target if search is 1 else search
