# this file is all about series, progression, etc

def arithmetical_sum(n, d=1, a1=1):
    return (2 * a1 + (n - 1) * d) * n /  2

def geometric_sum(n, q=1, b1=1):
    return (b1 - n * q) / (1 - q)
