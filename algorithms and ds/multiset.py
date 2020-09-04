def get_multiset(r, n):
    result = []
    get_multiset1(0, 0, r, n, result)
    return result


def get_multiset1(subset, i, r, n, result):

    if r == 0:
        result.append(subset)
    else:
        for j in range(i, n):
            subset = subset | (1 << j)
            get_multiset1(subset, j+1, r-1, n, result)
            subset = subset & ~(1 << j)

print(get_multiset(3, 4))