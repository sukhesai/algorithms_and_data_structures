import random


def qsort(arr, p, r):
    while p < r:
        q, t = partition(arr, p, r)
        if q - p > r - t - 1:
            qsort(arr, p, q)
            p = t + 1
        else:
            qsort(arr, t + 1, r)
            r = q


def partition(arr, p, r):
    swap(arr, random.randrange(p, r + 1), r)
    x = arr[r]
    i = p - 1
    t = i
    for j in range(p, r):
        if arr[j] < x:
            i += 1
            t += 1
            if i == t:
                swap(arr, i, j)
            else:
                swap2(arr, i, t, j)
        elif arr[j] == x:
            t += 1
            swap(arr, t, j)
    t += 1
    swap(arr, t, r)
    return i + 1, t


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def swap2(arr, i, t, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = arr[t]
    arr[t] = temp


a = [47, 40, 79, 79, 76, 63, 81, 8, 89, 44, 88, 7, 92, 85,
     54, 23, 6, 41, 28, 84, 47, 34, 31, 15, 91, 65, 65, 15,
     56, 78, 9, 69, 98, 74, 76, 33, 63, 22, 89, 75, 12, 34,
     83, 68, 4, 96, 32, 70, 65, 82, 37, 13, 94, 33, 38, 76,
     83, 88, 55, 7, 40, 1, 41, 84, 27, 45, 93, 62, 19, 33,
     33, 11, 55, 40, 36, 82, 91, 52, 51, 69, 32, 22, 89, 53,
     22, 31, 61, 32, 14, 60, 94, 26, 48, 25, 76, 62, 3, 3, 15, 87]
arr = []
qsort(a, 0, len(a) - 1)
print(a, arr)
