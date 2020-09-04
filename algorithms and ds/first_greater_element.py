import math


def first_greater(x, a):
    l = 0
    r = len(x)
    while l != r:
        m = l + math.floor((r - l)/2)
        print("here", l, m, r, x[m], a)
        if x[m] < a:
            l = m + 1
        else:
            r = m
    return l


x = [0, 2, 12]
a = 10
print(first_greater(x, a))
