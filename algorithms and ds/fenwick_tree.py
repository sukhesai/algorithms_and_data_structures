class fenwick_tree1:
    def __init__(self, a):
        self.tree = [0] + a
        self.construct()

    def construct(self):
        n = len(self.tree)
        for i in range(1, n):
            if i + lsb(i) < n:
                self.tree[i+lsb(i)] += self.tree[i]

    def prefix_sum(self, i):
        i += 1
        sum = 0
        while i != 0:
            sum += self.tree[i]
            i = i - lsb(i)
        return sum

    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i-1)

    def point_update(self, i, x):
        i += 1
        n = len(self.tree)
        while i < n:
            self.tree[i] += x
            i += lsb(i)


class fenwicktree2:

    def __init__(self, a):
        self.tree = [0]*(len(a)+1)

    def point_query(self, i):
        s = a[i]
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= lsb(i)
        return s

    def update_range(self, i, j, b):
        self.prefix_update(i, b)
        self.prefix_update(j+1, -b)

    def prefix_update(self, i, b):
        i += 1
        while i < len(self.tree):
            self.tree[i] += b
            i += lsb(i)


class fenwicktree22:

    def __init__(self, a):
        self.tree = [0, a[0]]
        for i in range(1, len(a)):
            self.tree.append(a[i]-a[i-1])
        for i in range(1, len(a)):
            if i + lsb(i) <= len(a):
                self.tree[i+lsb(i)] += self.tree[i]

    def point_query(self, i):
        s = 0
        i = i + 1
        while i > 0:
            s += self.tree[i]
            i -= lsb(i)
        return s

    def update_range(self, i, j, b):
        self.point_update(i, b)
        self.point_update(j+1, -b)

    def point_update(self, i, b):
        i += 1
        while i < len(self.tree):
            self.tree[i] += b
            i += lsb(i)


def lsb(i):
    return i & (-i)


a = [3, 2, 1, 0]
ft2 = fenwicktree22(a)
ft2.update_range(1, 2, 1)
print(ft2.tree)
for i in range(4):
    print(ft2.point_query(i))
