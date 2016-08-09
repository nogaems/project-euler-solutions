from utils.factorization import get_factor_list

dividers = []
for n in xrange(2, 21):
    factors = get_factor_list(n) 
    for f in factors:
        if f not in dividers:
            dividers += [f] * factors.count(f)
        else:
            if dividers.count(f) < factors.count(f):
                dividers += [f] * (factors.count(f) - dividers.count(f))

result = reduce(lambda x, y: x * y, dividers)
print(result)

