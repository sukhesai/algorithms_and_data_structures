

def countingsort(a):
    arraylength = len(a)
    i = max(a) + 1
    c = [-1]*i
    for j in range(arraylength):
        k = a[j]
        for m in range(k, i):
            c[m] += 1
        for m in range(j, c[k] - 1, -1):
            if m == 0:
                break
            a[m] = a[m - 1]
        a[c[k]] = k


arr = [47, 40, 79, 79, 76, 63, 81, 8, 89, 44, 88, 7, 92, 85,
       54, 23, 6, 41, 28, 84, 47, 34, 31, 15, 91, 65, 65, 15,
       56, 78, 9, 69, 98, 74, 76, 33, 63, 22, 89, 75, 12, 34,
       83, 68, 4, 96, 32, 70, 65, 82, 37, 13, 94, 33, 38, 76,
       83, 88, 55, 7, 40, 1, 41, 84, 27, 45, 93, 62, 19, 33,
       33, 11, 55, 40, 36, 82, 91, 52, 51, 69, 32, 22, 89, 53,
       22, 31, 61, 32, 14, 60, 94, 26, 48, 25, 76, 62, 3, 3, 15, 87]
b = []
k = 10
for i, e in enumerate(arr):
    b.append(e % k)
print(b, len(b))
countingsort(b)
print(b, len(b))
