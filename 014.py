collatz = lambda n: int(n/2) if n % 2 == 0 else int(n * 3 + 1)

chain = [1] * int(1e6)

for number in range(2,int(1e6)):
    temp = number
    while temp != 1:        
        temp = collatz(temp)
        if temp < number:
            chain[number] = chain[number] + chain[temp]
            break
        chain[number] = chain[number] + 1

print(chain.index(max(chain)))
        
