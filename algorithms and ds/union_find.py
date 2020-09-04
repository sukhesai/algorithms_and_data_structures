

class union_find:

    def __init__(self):
        self.parent = []
        self.components = 0
        self.rank = []
        # may keep size list in place of rank list if
        # we like to trace the size of each disjoint set

    def construct(self, n):
        self.parent = [i for i in range(n)]
        self.components = n
        self.rank = [0]*n

    def union(self, i, j):
        self.link(self.find(i), self.find(j))

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def link(self, i, j):
        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
        else:
            self.parent[i] = j
            if self.rank[i] == self.rank[j]:
                self.rank[j] += 1
        self.components -= 1


unionfind = union_find()
n = 10
unionfind.construct(n)
unionfind.union(1, 4)
unionfind.union(4, 9)
for i in range(10):
    print(unionfind.find(i))