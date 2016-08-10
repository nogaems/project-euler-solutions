# Approximation of function's local zero.
# Newton's method
def approx(x0, f, f1, e=1):
    while True:
        x1 = x0 - f(x0)/f1(x0)
        if abs(x1 - x0) <= e:
            return x1
        x0 = x1
