from utils.factorization import get_factor_list
from utils.sets import get_all_subsets
from utils.faulhaber import ff
from utils.soe2 import get_primes

num = 2
primes = get_primes(1000)

while True:
    triangle_number = ff(num)
    factors = get_factor_list(triangle_number, primes=primes)
    divisors = get_all_subsets(factors)
    if len(divisors) > 500:
        print(triangle_number)
        break
    num = num + 1

