import math

def get_triples(c_max=5):    
    """
    a^2 + b^2 = c^2
    a < b < c

    e.g 3^2 + 4^2 = 5^2
    """
    
    if not isinstance(c_max, int):
        raise TypeError('\'c_max\' must be \'int\'')
    elif c_max < 5:
        raise ValueError('\'c_max\' must be greater than \'4\'')
    
    f1 = lambda m, n: m ** 2 - n ** 2
    f2 = lambda m, n: 2 * m * n
    f3 = lambda m, n: m ** 2 + n ** 2

    triples = []
    m = 2
    
    while True:
        if m > int(math.sqrt(c_max - 1)):
            return triples
        for n in range(1, m):
            a, b, c = sorted([f1(m, n), f2(m, n), f3(m, n)])
            if c > c_max:
                break
            if  c % b != 0 and b % a != 0 and c % a != 0 and [a, b, c] not in triples:
                triples.append([a, b, c])
                k = 2
                while True:
                    a, b, c = a * k, b * k, c * k
                    if c > c_max:
                        break
                    elif [a, b, c] not in triples:
                        triples.append([a, b, c])
                    k += 1

        m += 1
