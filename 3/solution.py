from utils.soe2 import get_primes
from math import sqrt, ceil

target = 600851475143  # constant in conditions of problem
search = 1  # initial value
top_border = int(ceil(sqrt(600851475143)))  # the calculation of the upper limit of the required sequence of prime numbers
primes = get_primes(top_border)
for n in primes:
    while True:  # repeating the division as long as possible
        if target % n == 0: 
            target = target / n
            search = n
        else:
            break

print(search)
