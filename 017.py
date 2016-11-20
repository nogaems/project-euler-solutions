from utils.number import in_words

counter = 0

for n in range(1, 1001):
    counter = counter + len(in_words(n).replace(' ', '').replace('-', ''))

print(counter)
