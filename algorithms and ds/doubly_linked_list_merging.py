class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class dlinked_list:
    def __init__(self):
        self.head = None

    def insert(self, node):
        h = self.head
        if not h:
            self.head = node
            node.left = node
            node.right = node
            return
        next_node = h.right
        h.right = node
        node.left = h
        node.right = next_node
        next_node.left = node

    def merge(self, nlist):
        if not nlist.head:
            return
        h = self.head
        if not h:
            self.head = nlist
            return
        R1 = h
        r1 = h.right
        R2 = nlist.head
        r2 = R2.right
        R1.right = r2
        r2.left = R1
        R2.right = r1
        r1.left = R2

    def printlist(self):
        h = self.head
        print(h.data)
        while h.right != self.head:
            h = h.right
            print(h.data)


a = [i for i in range(5)]
fl = dlinked_list()
for i in a:
    # print(i)
    n = node(i)
    fl.insert(n)
    # print(n.data, n.left.data, n.right.data)

sl = dlinked_list()
print('1st')
fl.printlist()
for i in a:
    # print(i)
    n = node(i)
    sl.insert(n)
fl.merge(sl)
del sl
print('merged:')
fl.printlist()
print('second:')
sl.printlist()
