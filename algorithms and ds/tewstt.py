

def check(a):  # assuming n>=3
    n = len(a)
    if n < 3:
        return False
    fluctuation = 0
    d = a[0]
    for i in range(1, n):
        if a[i] - a[i-1] != d:
            if fluctuation == 0:
                fluctuation += 1
            else:
                return False
    print('returning')
    return a[-1] % a[0] == 0


def check1(a):
    if len(a) != 3:
        return False
    return (a[2]-a[1]) % a[0] == 0


def calc(a):
    d = a[1] // a[0]
    decr = (d-1)*a[0]
    a[1] -= decr
    a[2] -= decr
    return d-1


def sort_n_remove_duplicate(b):

    b.sort()
    c = []
    last = None
    for i in range(len(b)):
        if b[i] != last:
            c.append(b[i])
            last = b[i]
    return c


# strr = '17 33 65 129 257 513 1025 2049 4097 8193 16385 32769'
# strr = '1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768'
# strr = '5993 44000 50000 56000'
# strr = '367 717 1067 1417 1767 2117 2467 2817 3167 3517 3867 4217 4567 4917 5267 5617 5967 6317 6667 7017 7367 7717 8067 8417 8767 9117 9467 9817 10167 10517 10867 11217 11567 11917 12267 12617 12967 13317 13667 14017 14367 14717 15067 15417 15767 16117 16467 16817 17167 17517 17867 18217 18567 18917 19267 19617 19967 20317 20667 21017 21367 21717 22067 22417 22767 23117 23467 23817 24167 24517 24867 25217 25567 25917 26267 26617 26967 27317 27667 28017 28367 28717 29067 29417 29767 30117 30467 30817 31167 31517 31867 32217 32567 32917 33267 33617 33967 34317 34667 35017'
strr = '2 34 156'
# strr = '1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768'
'''with open('testfile.txt', 'r') as f:
    f.readline()
    strr = f.readline()'''
a = list(map(int, strr.split()))
a = sort_n_remove_duplicate(a)
print(len(a))
loop = 0
while len(a) != 0:
    if check1(a):
        loop += calc(a)
    if check(a):
        # print(a)
        loop += a[-1] // a[0]
        break
    print(a)
    b = []
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            b.append(-a[i]+a[j])
    loop += 1
    a = []
    a = sort_n_remove_duplicate(b)
    
print(loop)
