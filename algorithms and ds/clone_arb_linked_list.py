def copyList(head):
    c1 = head
    
    while c1:
        new = Node(c1.data)
        n1 = c1.next
        c1.next = new
        new.next = n1
        c1 = n1
    c1 = head
    headc = c1.next
    while c1:
        c2 = c1.next
        n1 = c2.next
        if n1:
            n2 = n1.next
        else:
            n2 = None
        if c1.arb:
            c2.arb = c1.arb.next

        c1 = n1
    
    c1 = head
    while c1:
        c2 = c1.next
        n1 = c2.next
        if n1:
            n2 = n1.next
        else:
            n2 = None
        c1.next = n1
        c2.next = n2
        c1 = n1
    return headc


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arb = None


class linkedlist:
    def __init__(self, data):
        new = Node(data)
        self.head = new
        self.tail = new

    def insert(self, data):
        new = Node(data)
        self.tail.next = new
        self.tail = new

    def setarb(self, n, i, j):
        c1 = self.head
        n = 1
        while n < i and c1:
            c1 = c1.next
            n += 1
        c2 = self.head
        n = 1
        while n < j and c2:
            c2 = c2.next
            n += 1
        if c1:
            c1.arb = c2
        # print('inserted arbitrary pointer', i, j)


def printlist(head):
    c = head
    # print('List elements:')
    elements = []
    while c is not None:
        elements.append(c.data)
        c = c.next
    c = head
    # print('Arbitrary pointers:')
    arbit = []
    while c is not None:
        if c.arb is not None:
            arbit.append(c.arb.data)
        else:
            arbit.append(None)
        c = c.next
    return elements, arbit


arr = list(map(int, input().split()))
mylist = linkedlist(arr[0])
n = len(arr)
print(n)
for i in range(1, n):
    mylist.insert(arr[i])

arr1 = list(map(int, input().split()))
pairs = len(arr1)

print(pairs, 'pairs')

for i in range(pairs//2):
    mylist.setarb(n, arr1[2*i], arr1[2*i+1])

a, b = printlist(mylist.head)
clonedlist = copyList(mylist.head)

c, d = printlist(clonedlist)
e, f = printlist(mylist.head)
if a != c:
    print('a!=c', a, c)
if a != e:
    print('a!=e', a, e)
if b != d:
    print('b!=d', b, d)
if b != f:
    print('b!=f', b, f)
