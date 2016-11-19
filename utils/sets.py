def get_all_subsets(source):
    if not isinstance(source, list):
        raise TypeError('\'source\' must be \'list\', not \'{}\''.format(source.__class__.__name__))

    result = [[]]    
    mask_top_border = 2**len(source)

    for mask in range(1, mask_top_border):
        subset = []
        for index in range(len(source)):
            if mask >> index & 1:
                subset.append(source[index])
            subset.sort()
            if not subset in result:
                result.append(subset)
    return result
