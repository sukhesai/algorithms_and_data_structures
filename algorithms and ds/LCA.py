class Node:

    def __init__(self, p=None, left=None, right=None, key=None, color=None):
        self.p = p
        self.left = left
        self.right = right
        self.key = key
        self.color = color


class RBTree:

    def __init__(self, node=None):

        self.nil = Node(color=1)
        if not node:
            self.root = self.nil
        else:
            self.root = node

    def leftrotate(self, x):

        y = x.right
        y.p = x.p
        x.right = y.left
        x.right.p = x
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightrotate(self, x):

        y = x.left
        y.p = x.p
        x.left = y.right
        x.left.p = x
        if y.p == self.nil:
            self.root = y
        elif y.p.left == x:
            y.p.left = y
        else:
            y.p.right = y
        x.p = y
        y.right = x

    def transplant(self, u, v):
        v.p = u.p
        if v.p == self.nil:
            self.root = v
        elif u == v.p.left:
            v.p.left = v
        else:
            v.p.right = v

    def insertnode(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if x.key >= z.key:
                x = x.left
            else:
                x = x.right
        if y == self.nil:
            self.root = z
        elif y.key >= z.key:
            y.left = z
        else:
            y.right = z
        z.p = y
        self.insertfixup(z)

    def insertfixup(self, z):
        while z.p.color == 0:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 0:
                    z.p.color = 1
                    z.p.p.color = 0
                    y.color = 1
                    z = y.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.leftrotate(z)
                    self.rightrotate(z.p.p)
                    z.p.color = 1
                    y.p.color = 0
            else:
                y = z.p.p.left
                if y.color == 0:
                    z.p.color = 1
                    z.p.p.color = 0
                    y.color = 1
                    z = y.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rightrotate(z)
                    self.leftrotate(z.p.p)
                    z.p.color = 1
                    y.p.color = 0
        self.root.color = 1

    def deletenode(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, x)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, x)
        else:
            y = self.successor(z)
            y_original_color = y.color
            x = y.right
            if y == z.right:
                x.p = y
            else:
                self.transplant(y, x)
                z.right.p = y
                y.right = z.right
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 1:
            self.deletefixup(x)

    def deletefixup(self, x):
        while x != self.root and x.color == 1:
            if x == x.p.left:
                w = x.p.right
                if w.color == 0:
                    self.leftrotate(x.p)
                    x.p.color = 0
                    w.color = 1
                else:
                    if w.left.color == 1 and w.right.color == 1:
                        w.color = 0
                        x = x.p
                    elif w.left.color == 0 and w.right.color == 1:
                        self.rightrotate(w)
                        w.color = 0
                        w.p.color = 1
                    else:
                        self.leftrotate(x.p)
                        w.color = x.p.color
                        x.p.color = 1
                        w.right.color = 1
                        x = self.root
            else:
                w = x.p.left
                if w.color == 0:
                    self.rightrotate(x.p)
                    x.p.color = 0
                    w.color = 1
                else:
                    if w.left.color == 1 and w.right.color == 1:
                        w.color = 0
                        x = x.p
                        x.color = 1
                    elif w.right.color == 0 and w.left.color == 1:
                        self.leftrotate(w)
                        w.color = 0
                        w.p.color = 1
                    else:
                        self.rightrotate(x.p)
                        w.color = x.p.color
                        x.p.color = 1
                        w.left.color = 1
                        x = self.root
        x.color = 1

    def insertkey(self, key):
        z = Node(key=key, color=0, left=self.nil, right=self.nil)
        self.insertnode(z)
        return z

    def deletekey(self, key):
        x = self.root
        while x != self.nil:
            if x.key == key:
                self.deletenode(x)
                return "key deleted successfully!"
            elif x.key < key:
                x = x.right
            else:
                x = x.left
        return "Key not found!"

    def maximum(self, x):
        while x != self.nil:
            y = x
            x = x.right
        return y

    def minimum(self, x):
        while x != self.nil:
            y = x
            x = x.left
        return y

    def successor(self, x):
        if x.right != self.nil:
            return self.minimum(x.right)
        else:
            y = x.p
            while y != self.nil and y.right == x:
                x = y
                y = y.p
            return y

    def predecessor(self, x):
        if x.left != self.nil:
            return self.maximum(x.right)
        else:
            y = x.p
            while y != self.nil and y.left == x:
                x = y
                y = y.p
            return y

    def inorderwalk(self, x=None):
        if not x:
            x = self.root
        if x == self.nil:
            return
        self.inorderwalk(x.left)
        print(x.key)
        self.inorderwalk(x.right)


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

    def add(self):
        total_elements = len(self.parent)
        self.parent.append(total_elements)
        self.rank.append(0)
        self.components += 1
        return total_elements


def LCA(root, ancestors, key_to_node_map, visited, node_to_key_map):
    key = uf.add()
    key_to_node_map[key] = root
    node_to_key_map[root] = key
    ancestors[root] = root  # node to node relation can also be used
    # print("key:", key, "node:", root.key, 'visited:', visited)
    if root.left != mytree.nil:
        LCA(root.left, ancestors, key_to_node_map, visited, node_to_key_map)
        key_left = node_to_key_map[root.left]
        uf.union(key_left, key)
        # print('united {} and {}'.format(key_to_node_map[key_left].key, key_to_node_map[key].key))
        ancestors[key_to_node_map[uf.find(key)]] = root
        # print('ancestor of united group is:', ancestors[key_to_node_map[uf.find(key_left)]].key)
    if root.right != mytree.nil:
        LCA(root.right, ancestors, key_to_node_map, visited, node_to_key_map)
        key_right = node_to_key_map[root.right]
        uf.union(key_right, key)
        # print('united {} and {}'.format(key_to_node_map[key_right].key, key_to_node_map[key].key))
        ancestors[key_to_node_map[uf.find(key)]] = root
        # print('ancestor of united group is:', ancestors[key_to_node_map[uf.find(key_right)]].key)
    visited[key] = True
    # print('visited both children of {}. Ancestors of each node is:'.format(root.key))
    # for i in ancestors:
        # print('ancsetor of {} is {}'.format(i.key, ancestors[key_to_node_map[uf.find(node_to_key_map[i])]].key))
    # print('visited list is:', visited)
    for i in s:
        if i[0] == root:
            v = i[1]
        elif i[1] == root:
            v = i[0]
        else:
            v = None
        try:
            if visited[node_to_key_map[v]]:
                repr = key_to_node_map[uf.find(node_to_key_map[v])]
                print('least commomn ancestor of {} and {} is {}'.format(i[0].key, i[1].key, ancestors[repr].key))
        except KeyError:
            pass
mytree = RBTree()
a = [8, 4, 12, 1, 5, 9]
nodes = []
for i in a:
    nodes.append(mytree.insertkey(i))

# mytree.inorderwalk()
s = [(nodes[3], nodes[4]), (nodes[3], nodes[5]), (nodes[4], nodes[5]), (nodes[1], nodes[4])]
uf = union_find()
key_to_node_map = dict()
ancestors = dict()
visited = [False]*len(a)
node_to_key_map = dict()
LCA(mytree.root, ancestors, key_to_node_map, visited, node_to_key_map)
# for i in range(6):
#    print(ancestors[key_to_node_map[uf.find(node_to_key_map[nodes[1]])]].key)
