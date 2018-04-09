from utils.number import in_words

print(sum([len(in_words(n).replace(' ', '').replace('-', ''))
           for n in range(1, 1001)]))
