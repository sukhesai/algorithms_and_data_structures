gap = 5
a = [62, 83, 18, 57, 7, 17, 95, 86, 47, 69, 25, 28]
length = len(a)
for i in range(gap, length):
    temp = a[i]
    j = i - gap
    while a[j] > temp and j >= 0:
        a[j + gap] = a[j]
        j -= gap
    a[j + gap] = temp
print(a)