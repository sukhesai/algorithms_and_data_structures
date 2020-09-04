import math


class ipq:
    def __init__(self, d):
        self.tree = []
        self.d = d
        self.prt = []
        self.pos = []

    def get_size(self):
        return len(self.tree)

    def insert(self, key, p):
        self.tree.append(key)
        if len(self.pos) > key:
            self.pos[key] = self.get_size() - 1
        else:
            while len(self.pos) < key:
                self.pos.append(None)
            self.pos.append(self.get_size()-1)
        if len(self.prt) > key:
            self.prt[key] = p
        else:
            while len(self.prt) < key:
                self.prt.append(None)
            self.prt.append(p)
        self.bubbleup(self.get_size()-1)

    def bubbleup(self, i):
        if i <= 0:
            return
        p = (i-1)//self.d
        if self.prt[self.tree[p]] > self.prt[self.tree[i]]:
            self.swap(i, p)
            self.bubbleup(p)

    def swap(self, i, j):
        self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
        self.pos[self.tree[i]], self.pos[self.tree[j]] = self.pos[self.tree[j]], self.pos[self.tree[i]]

    def poll(self):
        if self.get_size() == 0:
            return None
        if self.get_size() == 1:
            return self.tree.pop()
        z = self.tree[0]
        self.tree[0] = self.tree.pop()
        self.pos[self.tree[0]] = 0
        self.bubbledown(0)
        return z

    def bubbledown(self, i):
        minimum = i
        for j in range(self.d):
            child = i*self.d + j + 1
            if child < self.get_size() and self.prt[self.tree[child]] < self.prt[self.tree[minimum]]:
                minimum = child
        if i != minimum:
            self.swap(i, minimum)
            self.bubbledown(minimum)

    def decreasepri(self, key, np):
        if len(self.prt) <= key or self.prt[key] < np:
            return
        self.prt[key] = np
        self.bubbleup(self.pos[key])


def dijkstra(a):
    n = len(g)
    distance = [math.inf]*n
    distance[a] = 0
    d = no_of_edges//no_of_nodes
    pq = ipq(d)
    pq.insert(a, 0)
    while pq.get_size() > 0:
        curr  = pq.poll()
        print("minimum node is {} with value {}".format(curr, distance[curr]))
        print("size of pq is:", pq.get_size())
        for next_node in g[curr]:
            print("its next nodes:", next_node[0])
            if distance[next_node[0]] == math.inf:
                distance[next_node[0]] = next_node[1] + distance[curr]
                pq.insert(next_node[0], distance[next_node[0]])
                print("insert new {} node with value {}".format(next_node[0], distance[next_node[0]]))
            elif  next_node[1] + distance[curr] < distance[next_node[0]]:
                distance[next_node[0]] = next_node[1] + distance[curr]
                pq.decreasepri(next_node[0], distance[next_node[0]])
                print("decrease dist of node {} to {}".format(next_node[0], distance[next_node[0]]))

    return distance


g = (((1, 4), (2, 1)), ((3, 1), ), ((1, 2), (3, 5)), ((4, 3), ), ())
no_of_edges = 6
no_of_nodes = 5
print(dijkstra(0))
