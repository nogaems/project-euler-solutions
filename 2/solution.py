result = 0
a, b = 1, 2
while a <= 4000000:
    a, b = b, a + b
    if a % 2 == 0:
        result = result + a

print(result)
