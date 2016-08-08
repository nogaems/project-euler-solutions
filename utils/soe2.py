# optimized  implementation of sieve of Eratosthene
def get_primes(N):
    """
    returns list of prime numbers up to N
    @param N: top border
    @type N: int
    @rtype: list
    
    """    
    N = int(N)
    sieve = [True] * (N + 1)
    prime = 2  # initial value
    while N + 1 >= prime ** 2:
        for i in xrange((prime ** 2) - 2, N + 1, prime): # for all numbers which multiples of "prime"
            sieve[i] = False
        for n in xrange(prime - 1, N + 1):  # definition of next prime number 
            if sieve[n]:
                prime = n + 2
                break
    result = []
    for i in xrange(N):
        if sieve[i]:
            result.append(i+2)
    return result

def dump(data, path='primes.data', separator='\n'):
    """
    Makes dump to the file
    Returns True if successful, else False
    @param data: list with prime numbers
    @type data: list
    @param path: string containing the path to the output file
    @type path: basestring
    @param separator: separation character or string
    @type separator: basestring
    @rtype: Bool
    """
    with open(path, 'w') as out:
        try:
            out.write('\n'.join(map(lambda ch: str(ch), data)))
            out.flush()
            out.close()
            return True
        except Exception as e:
            print(e)
            return False
  
