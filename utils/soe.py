# simple implementation of sieve of Eratosthene

def get_primes(N):
    """
    returns list of prime numbers up to N
    @param N: top border
    @type N: int
    @rtype: list
    
    """    
    N = int(N)
    sieve = [n for n in range(2, N + 1)]  # list of integers in [2, N]
    prime = 2  # initial value
    while len(sieve) >= prime ** 2:
        for i in [sieve.index(n) for n in sieve[(prime ** 2) - 2::prime]]:  # computation of the mask
            sieve[i] = None  # applying of the mask
        for n in sieve[sieve.index(prime) + 1:]:  # definition of next prime number 
            if n is not None:
                prime = n
                break
    return filter(None, sieve)
