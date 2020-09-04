

def select(left, right, n):
    while True:
        if left == right:
            return left
        pivotIndex = pivot(left, right)
        pivotIndex, pivotIndexEq = partition(left, right, pivotIndex)
        if n < pivotIndex:
            right = pivotIndex - 1
        elif n <= pivotIndexEq:
            return n
#        n -= (left - pivotIndex + 1)
        else:
            left = pivotIndexEq + 1


def partition(left, right, pivotIndex):
    swap(right, pivotIndex)
    pivotIndex = left
    pivotvalue = a[right]
    for i in range(left, right):
        if a[i] < pivotvalue:
            swap(i, pivotIndex)
            pivotIndex += 1
    pivotIndexEq = pivotIndex
    for i in range(pivotIndex, right):
        if a[i] == pivotvalue:
            swap(i, pivotIndexEq)
            pivotIndexEq += 1
    swap(pivotIndexEq, right)
    return pivotIndex, pivotIndexEq


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
        mid = (no_of_subgrps + 1)//2
        return select(left, left + no_of_subgrps - 1, mid)


def partition5(left, right):
    for i in range(left + 1, right + 1):
        temp = a[i]
        for j in range(i - 1, left - 1, -1):
            if a[j] > temp:
                a[j + 1] = a[j]
            else:
                break
        a[j + 1] = temp
    return (left + right) // 2


a = [1, 2, 3, 2, 1, 8, 4, 2]
#for i in range(1, 9):
#    print(a[select(0, 7, 1)])
print(a[select(5, 7, 5)])
