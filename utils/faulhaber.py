def ff(n, p=1):
    n = int(n)
    """
    the sum of the p-th powers of the first n positive integers

    """
    if p is 1:
        result = (n**2 + n) / 2
    elif p is 2:
        result =  (2 * n**3 + 3 * n**2 + n) / 6
    elif p is 3:
        result = (n**4 + 2 * n**3 + n**2) / 4
    elif p is 4:
        result = (6 * n**5 + 15 * n**4 + 10 * n**3 - n) / 30
    elif p is 5:
        result =  (2 * n**6 + 6 * n**5 + 5 * n**4 - n**2) / 12
    elif p is 6:
        result =  (6 * n**7 + 21 * n**6 + 21 * n**5 - 7 * n**3 + n) / 42
    else:
        return None
    return int(result)
