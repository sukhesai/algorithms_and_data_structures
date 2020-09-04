

class ipq():
    def __init__(self):
        self.tree = []  # tree in from of array to store key_index of elements
        self.count = 0
        self.priority = []
        # priority[key_index] = priority of that key
        self.pos = []
        # position of key_index in tree

    def construct(self, arr, pri):
        # arr should contain [0,..,n-1] in any oreder
        self.tree = list(arr)
        self.priority = list(pri)
        self.count = len(arr)
        self.pos = [None]*self.count
        for i, e in enumerate(arr):
            self.pos[e] = i
        # print('initial pos', self.pos)
        for i in range((self.count-2)//2, -1, -1):
            # print('bubbling down ', i)
            self.bubbledown(i)
            # print('after bublling down', self.tree, self.pos)

    def swap(self, i, j):
        temp = self.tree[i]
        self.tree[i] = self.tree[j]
        self.tree[j] = temp
        pos_i = self.tree[i]
        pos_j = self.tree[j]
        temp = self.pos[pos_i]
        self.pos[pos_i] = self.pos[pos_j]
        self.pos[pos_j] = temp

    def bubbledown(self, i):
        while i < self.count:
            lchild = 2*i + 1
            if lchild > self.count-1:
                break
            rchild = 2*i + 2
            if rchild > self.count-1:
                rchild = None
            m = lchild
            if rchild and self.priority[self.tree[rchild]] < self.priority[self.tree[lchild]]:
                m = rchild
            if self.priority[self.tree[m]] < self.priority[self.tree[i]]:
                self.swap(i, m)
                i = m
            else:
                break

    def bubbleup(self, i):
        p = (i-1)//2
        while i != 0 and self.priority[self.tree[i]] < self.priority[self.tree[p]]:
            self.swap(i, p)
            i = p
            p = (p-1)//2

    def poll(self):
        if self.count == 0:
            return "queue is empty"
        if self.count == 1:
            z = self.tree.pop()
            self.count = 0
            return z
        z = self.tree[0]
        self.tree[0] = self.tree.pop()
        self.pos[self.tree[0]] = 0
        self.count -= 1
        self.bubbledown(0)
        return z


arr = [1, 4, 2, 3, 0]
priority = [6, 2, 1, 2, -1]
my_pq = ipq()
my_pq.construct(arr, priority)
print(my_pq.tree)
print(my_pq.pos)
print(my_pq.priority)
for i in range(6):
    print(my_pq.poll())
