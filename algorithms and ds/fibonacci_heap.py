import math


class node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.left = None
        self.right = None
        self.parent = None
        self.child = None


def merge_lists(list1, list2):        # merge list2 in list1
    R1 = list1.root
    R2 = list2.root
    list1.total += list2.total
    if not R2:
        return
    if not R1:
        list1.root = R2
        return
    r1 = R1.right
    r2 = R2.right
    R1.right = r2
    r2.left = R1
    R2.right = r1
    r1.left = R2
    if R1.key > R2.key:
        list1.root = R2


class fib_heap:
    def __init__(self):
        self.root = None
        self.total = 0

    def insert(self, nod):
        self.total += 1
        if not self.root:
            self.root = nod
            nod.left = nod
            nod.right = nod
            return
        next_node = self.root.right
        nod.right = next_node
        next_node.left = nod
        self.root.right = nod
        nod.left = self.root
        if self.root.key > nod.key:
            self.root = nod

    def merge(self, heap):
        merge_lists(self, heap)

    def pop_min(self):
        z = self.root
        if not z:
            return None
        self.total -= 1
        if z.child:
            new_heap = fib_heap()
            new_heap.root = z.child
            z.child.parent = None
            z.child = None
            self.merge(new_heap)
            self.root = z
        if z == z.right:
            self.root = None
        else:
            self.root = z.right
            left_node = z.left
            left_node.right = self.root
            self.root.left = left_node
            if self.root != self.root.right:
                self.consolidate()
        z.left = None
        z.right = None
        return z

    def consolidate(self):
        n = math.floor(math.log(self.total+1)/math.log(1.6))
        a = [None]*n
        x = self.root
        temp_root = x
        last_node = x.left
        a[x.degree] = x
        x = x.right
        last_flag = True
        while last_flag:
            if x == last_node:
                last_flag = False
            d = x.degree
            n_node = x.right
            if not a[d]:
                a[d] = x
                if temp_root.key > x.key:
                    temp_root = x
            else:
                y = a[d]
                if y.key < x.key:
                    temp = x
                    x = y
                    y = temp
                self.plant(y, x)
                if temp_root.key > x.key:
                    temp_root = x
                x.degree += 1
                a[x.degree-1] = None
                a[x.degree] = x
            x = n_node
        self.root = temp_root

    def plant(self, y, x):
        left_node = y.left
        right_node = y.right
        left_node.right = right_node
        right_node.left = left_node
        child = x.child
        if child:
            right = child.right
            child.right = y
            y.left = child
            right.left = y
            y.right = right
        else:
            x.child = y
            y.left = y
            y.right = y
        y.mark = False

    def decrease_key(self, nod, new_key):
        if new_key > nod.key:
            return "new key greater than original"
        nod.key = new_key
        p = nod.parent
        if p and p.key > new_key:
            self.cut(p, nod)
            self.cascadecut(p)
        if self.root.key > new_key:
            self.root = nod

    def cut(self, p, c):
        c.parent = None
        c.mark = False
        if p.degree == 1:
            p.child = None
        else:
            right_node = c.right
            left_node = c.left
            left_node.right = right_node
            right_node.left = left_node
            p.child = right_node
            right_node.parent = p
        p.degree -= 1
        right_node = self.root.right
        right_node.left = c
        c.right = right_node
        self.root.right = c
        c.left = self.root

    def cascadecut(self, p):
        z = p.parent
        if z:
            if not p.mark:
                p.mark = True
            else:
                self.cut(z, p)
                self.cascadecut(z)

    def delete_key(self, node):
        self.decrease_key(node, -math.inf)
        self.pop_min()


myheap = fib_heap()
for i in range(5):
    myheap.insert(node(i))

for i in range(1):
    print(myheap.pop_min().key)

for i in range(5):
    myheap.insert(node(-i))
n = node(10)
myheap.insert(n)
myheap.decrease_key(n, -10)
myheap.delete_key(n)

for i in range(9):
    print(myheap.pop_min().key)
