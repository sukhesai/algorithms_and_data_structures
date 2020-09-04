

class IPQ:
    def __init__(self, d):
        self.pos = []
        self.pri = []
        self.d = d
        self.tree = []

    def get_size(self):
        return len(self.tree)

    def insert(self, id, p):
        self.tree.append(id)
        if id > len(self.pos):
            while len(self.pos) != id:
                self.pos.append(None)
        if id == len(self.pos):
            self.pos.append(self.get_size()-1)
        else:
            self.pos[id] = self.get_size()-1
        if id > len(self.pri):
            while len(self.pri) != id:
                self.pri.append(None)
        if id == len(self.pri):
            self.pri.append(p)
        else:
            self.pri[id] = p
        self.bubbleup(self.get_size()-1)

    def bubbleup(self, i):
        p = (i-1) // self.d
        while p >= 0 and self.pri[self.tree[i]] < self.pri[self.tree[p]]:
            self.swap(i, p)
            i = p
            p = (p-1) // self.d

    def poll(self):
        if self.get_size() == 0:
            return None
        if self.get_size() == 1:
            z = self.tree.pop()
            p = self.pri[z]
            return z, p
        z = self.tree[0]
        p = self.pri[z]
        self.swap(0, -1)
        del self.tree[-1]
        self.bubbledown(0)
        return z, p

    def bubbledown(self, i):
        s = self.get_size()
        minimum = i
        k = 1
        while i*self.d + k < s and k <= self.d:
            if self.pri[self.tree[i*self.d + k]] < self.pri[self.tree[minimum]]:
                minimum = i*self.d + k
            k += 1
        if minimum != i:
            self.swap(minimum, i)
            self.bubbleup(minimum)

    def decrease_pri(self, id, p):
        if id >= len(self.pos) or self.pos[id] is None or self.pos[id] > self.get_size() - 1:
            return "Does not contain this id"
        if self.pri[id] <= p:
            return "new priority is not less than current priority"
        self.pri[id] = p
        self.bubbleup(self.pos[id])

    def swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
        self.pos[self.tree[i]], self.pos[self.tree[j]] = self.pos[self.tree[j]], self.pos[self.tree[i]]


def prims(s=0):
    ipq = IPQ(2)
    visited[s] = True
    visited_edges = 0
    mst = []
    for next_node in g[s]:
        parent[next_node[0]] = s
        IsInipq[next_node[0]] = True
        ipq.insert(next_node[0], next_node[1])
    while ipq.get_size() != 0 and visited_edges < n - 1:
        node, cost = ipq.poll()
        mst.append((parent[node], node, cost))
        IsInipq[node] = False
        visited[node] = True
        for next_node in g[node]:
            if not visited[next_node[0]]:
                if IsInipq[next_node[0]]:
                    if ipq.pri[next_node[0]] > next_node[1]:
                        ipq.decrease_pri(next_node[0], next_node[1])
                        parent[next_node[0]] = node
                else:
                    ipq.insert(next_node[0], next_node[1])
                    IsInipq[next_node[0]] = True
                    parent[next_node[0]] = node
        visited_edges += 1
    print(mst)


g = [[[2, 0], [5, 7], [3, 5], [1, 9]],
     [[0, 9], [3, -2], [6, 4], [4, 3]],
     [[0, 0], [5, 6]],
     [[0, 5], [1, -2], [5, 2], [6, 3]],
     [[1, 3], [6, 6]],
     [[2, 6], [0, 7], [3, 2], [6, 1]],
     [[5, 1], [3, 3], [1, 4], [4, 6]]]
n = 7
visited = [False]*n
parent = [None]*n
IsInipq = [False]*n
prims()
