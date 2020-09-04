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
            return self.tree.pop()
        z = self.tree[0]
        self.swap(0, -1)
        del self.tree[-1]
        self.bubbledown(0)
        return z

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
