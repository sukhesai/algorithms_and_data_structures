

def FFT(p, inv=False):
    length = 1
    a = (1 << 2)
    b = 2*a
    while length <= a:
        for i in range(0, b, 2*length):
            for j in range(0, length):
                u = p[i+j]
                v = p[i+j+length]
                p[i+j] = u + v
                p[i+j+length] = u - v
        length <<= 1
    if inv:
        for i in range(b):
            p[i] = (p[i] >> 3)
    return p


a = [1, 2, 3, 4]
p = [0, 2, 2, 1, 1, 0, 0, 0]
fftp = FFT(p)
print(fftp)
for i in range(len(fftp)):
    fftp[i] = fftp[i]**2
res = FFT(fftp, inv=True)
print(res)
