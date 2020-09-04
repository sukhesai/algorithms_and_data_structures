import random


def select(left, right, n):
    while True:
        if left == right:
            return left
        pivotIndex = pivot(left, right)
        pivotIndex, ps = partition(left, right, pivotIndex)
        t = n + ps
        w = a[pivotIndex][1]
        if t < 0.5:
            if t + w >= 0.5:
                return pivotIndex
            else:
                left = pivotIndex + 1
                n = t + w
        else:
            right = pivotIndex - 1


def partition(left, right, pivotIndex):
    swap(right, pivotIndex)
    pivotIndex = left
    pivotvalue = a[right][0]
    ps = 0
    for i in range(left, right):
        if a[i][0] < pivotvalue:
            ps += a[i][1]
            swap(i, pivotIndex)
            pivotIndex += 1
    swap(pivotIndex, right)
    print(pivotIndex, ps)
    return pivotIndex, ps


def swap(i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def pivot(left, right):
    if right - left < 5:
        return partition5(left, right)
    for i in range(left, right + 1, 5):
        subright = i + 4
        if subright > right:
            subright = right
        median = partition5(i, subright)
        swap(median, left + (i - left)//5)
    no_of_subgrps = (i - left)//5 + 1
    if no_of_subgrps < 6:
        return partition5(left, left + no_of_subgrps - 1)
    else:
        return random.randrange(left, left + no_of_subgrps)


def partition5(left, right):
    for i in range(left + 1, right + 1):
        temp = a[i]
        for j in range(i - 1, left - 1, -1):
            if a[j][0] > temp[0]:
                a[j + 1] = a[j]
            else:
                break
        a[j + 1] = temp
    return (left + right) // 2


a = [(69, 0.01125), (97, 0.0175), (82, 0.0175), (57, 0.01125),
     (20, 0.01125), (83, 0.005), (3, 0.005), (26, 0.01125), (51, 0.005),
     (59, 0.005), (41, 0.005), (31, 0.01125), (76, 0.005), (44, 0.0175),
     (23, 0.005), (56, 0.005), (65, 0.005), (66, 0.0175), (91, 0.0175),
     (13, 0.005), (47, 0.01125), (36, 0.005), (8, 0.01125), (71, 0.0175),
     (78, 0.01125), (12, 0.005), (25, 0.0175), (14, 0.005), (74, 0.005),
     (1, 0.01125), (77, 0.0175), (10, 0.01125), (45, 0.01125),
     (58, 0.01125), (95, 0.005), (88, 0.0175), (11, 0.005),
     (28, 0.01125), (16, 0.01125), (21, 0.0175), (61, 0.01125),
     (37, 0.005), (40, 0.005), (72, 0.005), (86, 0.01125),
     (2, 0.0175), (22, 0.0175), (70, 0.01125), (94, 0.005),
     (63, 0.0175), (99, 0.005), (89, 0.0175), (38, 0.0175),
     (4, 0.005), (6, 0.01125), (32, 0.005), (34, 0.005), (75, 0.01125),
     (7, 0.005), (15, 0.01125), (60, 0.01125), (68, 0.005), (33, 0.005),
     (53, 0.005), (48, 0.01125), (35, 0.005), (18, 0.0175),
     (24, 0.01125), (29, 0.005), (54, 0.01125), (98, 0.005),
     (39, 0.01125), (30, 0.01125), (87, 0.005), (52, 0.01125),
     (17, 0.005), (93, 0.01125), (85, 0.0175), (27, 0.005), (81, 0.0175),
     (5, 0.01125), (9, 0.005), (42, 0.01125), (49, 0.005), (46, 0.0175),
     (79, 0.01125), (67, 0.005), (62, 0.005), (73, 0.01125), (43, 0.005),
     (64, 0.01125), (80, 0.01125), (90, 0.01125), (96, 0.01125), (19, 0.0175),
     (100, 0.01125), (55, 0.01125), (92, 0.01125), (50, 0.01125), (84, 0.005)]


print(a[select(0, 99, 0)])
