from utils.pythagor import get_triples

const = 1000

for t in get_triples(const - 2):
    if t[0] + t[1] + t[2] == 1000:
        print(t[0] * t[1] * t[2])
