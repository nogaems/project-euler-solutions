# Sum of the p-th powers of the first n positive integers
# I got this expression through the analytical decision of Faulhaber's formula at p=2 

n = 100  # from the conditions of the problem

squares_sum = lambda n: (2 * n ** 3 + 3 * n ** 2 + n) / 6

from utils.series import arithmetical_sum

result = arithmetical_sum(n) ** 2 - squares_sum(n)
print(int(result))
