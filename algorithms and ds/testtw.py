a = [3, 37, 40, 45]

loop = 0
while len(a) != 0:
    print(a)
    b = set()
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            b.add(-a[i]+a[j])
    loop += 1
    a = list(b)
    a.sort()
print(loop)

