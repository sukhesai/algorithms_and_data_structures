class fenwick2:
    def __init__(self, a):
        self.b = list(a)
        for i in range(1, len(a)):
            self.b[i] += self.b[i-1]
        self.ft1 = [0]*(len(a)+1)
        self.ft2 = [0]*(len(a)+1)

    def range_update(self, i, j, v):
        # i, j are 0 based index referring to original array
        self.update_point1(i, v)
        self.update_point1(j+1, -v)
        self.update_point2(i, -v*i)
        self.update_point2(j+1, v*(j+1))

    def update_point1(self, i, v):
        i += 1
        while i < len(self.ft1):
            self.ft1[i] += v
            i += lsb(i)

    def update_point2(self, i, v):
        i += 1
        while i < len(self.ft1):
            self.ft2[i] += v
            i += lsb(i)

    def range_query(self, i, j):
        if i <= 0:
            return self.prefix_sum(j)
        return self.prefix_sum(j) - self.prefix_sum(i-1)

    def prefix_sum(self, i):
        return self.b[i] + self.prefix_sum1(i)*(i+1) + self.prefix_sum2(i)

    def prefix_sum1(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.ft1[i]
            i -= lsb(i)
        return s

    def prefix_sum2(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.ft2[i]
            i -= lsb(i)
        return s


def lsb(i):
    return i & (-i)


a = [3, 2, 1, 0]
f = fenwick2(a)
print(f.b)
f.range_update(1, 2, 1)
print(f.ft1, f.ft2)
for i in range(3):
    print(f.range_query(i, i+1))
