from utils.newton import approx
from utils.soe2 import get_primes

import math

a = 10001  # from the problem condition
f = lambda x: x / math.log(x, math.e) - a
f1 = lambda x: (math.log(x, math.e) - 1) / math.log(x, math.e) ** 2  # has been calculated analytically
print(get_primes(approx(a, f, f1))[10000])
