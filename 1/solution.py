from functools import reduce  # Fuck you Gvido 
print(reduce(lambda x, y: x + y, [n for n in range(1000) if n % 3 == 0 or n % 5 == 0]))

