def binary():
    l = 0
    r = len(x) - 1
    while l <= r:
        m = l + (r - l)//2
        if x[m] == a:
            return m
        elif x[m] < a:
            l = m + 1
        else:
            r = m - 1
    return -1


x = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
a = 7
print(binary())
