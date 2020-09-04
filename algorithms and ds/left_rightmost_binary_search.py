import math


def binary_leftmost(l, r):
    while l != r:
        m = l + math.floor((r - l)/2)
        if x[m] < a:
            l = m + 1
        else:
            r = m
    if x[l] == a:
        return l
    return l


def binary_rightmost(l, r):
    while l != r:
        m = l + math.ceil((r - l)/2)
        if x[m] > a:
            r = m - 1
        else:
            l = m
    if x[l] == a:
        return l
    return -1


x = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 8, 9]
a = 7.5
print(binary_leftmost(0, 14), binary_rightmost(0, 14))
