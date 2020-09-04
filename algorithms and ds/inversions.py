import math


def mergesort(a, p, r):
    if p < r:
        q = p + (r - p)//2
        n1 = mergesort(a, p, q)
        n2 = mergesort(a, q + 1, r)
        n3 = merge(a, p, q, r)
        return n1 + n2 + n3
    else:
        return 0


def merge(a, p, q, r):
    la = list(a[p:q + 1]) + [math.inf]
    ra = list(a[q + 1:r + 1]) + [math.inf]
    i = 0
    j = 0
    n = 0
    n1 = q - p + 1
    for k in range(p, r + 1):
        if la[i] <= ra[j]:
            a[k] = la[i]
            i += 1
        else:
            a[k] = ra[j]
            j += 1
            n += (n1 - i)
    return n


arr = [1, 5, 2, 7, 33, 7, 4, 2, 9]
n = mergesort(arr, 0, len(arr) - 1)
print(n)
