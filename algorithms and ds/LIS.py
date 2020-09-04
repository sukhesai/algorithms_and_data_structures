import math


def get_LIS(x):
    n = len(x)
    LIS_till = [[x[0]]]
    last_elements = [x[0]]
    for i in range(1, n):
        pos = first_greater(last_elements, x[i]) - 1
        # print(LIS_till, last_elements, i, x[i], pos)
        try:
            LIS_till[pos+1] = list(LIS_till[pos] + [x[i]])
        except IndexError:
            LIS_till.append(list(LIS_till[pos] + [x[i]]))
        try:
            last_elements[pos+1] = x[i]
        except IndexError:
            last_elements.append(x[i])
    return LIS_till[-1]


def first_greater(array, a):
    lft = 0
    rt = len(array)
    while lft != rt:
        m = lft + math.floor((rt - lft)/2)
        # print("here", lft, m, rt, array[m], a)
        if array[m] < a:
            lft = m + 1
        #    print("if block")
        else:
            rt = m
        #    print("else")
        # print("last", lft, m, rt)
    # print(array, a, lft)
    return lft


x = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(get_LIS(x))
