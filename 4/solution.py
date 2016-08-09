
def check(number):
    if len(str(number)) != 6:
        return False
    left, right = str(number)[:3], str(number)[3:]
    if left ==	right[::-1]:
      	return True
    else:
        return False

def process():
    search = {
        'value': 0,
        'f1': 0,
        'f2': 0
    }

    for f1 in xrange(101, 1000):
        for f2 in xrange(101, 1000):
            candidate = f1 * f2
            if check(candidate) and candidate > search['value']:
                search['value'] = candidate
                search['f1'], search['f2'] = f1, f2

    return search

print(process())
