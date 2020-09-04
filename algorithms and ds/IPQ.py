

class indexedPQ:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.pr = []
        self.pm = []

    def swap(self, i, p):
        ki_at_i = self.arr[i]
        ki_at_p = self.arr[p]
        self.arr[i] = ki_at_p
        self.arr[p] = ki_at_i
        self.pm[ki_at_i] = p
        self.pm[ki_at_p] = i

    def bubbleup(self, i):    # i is position of element in arr
        parent = (i-1)//2     # parent is position of parent of i
        x = self.arr[i]       # x is key index of element at position i
        while i > 0 and self.pr[x] < self.pr[self.arr[parent]]:
            self.swap(i, parent)
            i = parent
            parent = (i-1)//2

    def bubbledown(self, i):
        x = self.arr[i]
        left = 2*i+1
        right = left+1
        while left < self.size:
            if left == self.size-1:
                if self.pr[x] > self.pr[self.arr[left]]:
                    self.swap(i, left)
                return
            else:
                if self.pr[self.arr[left]] <= self.pr[self.arr[right]]:
                    if self.pr[self.arr[left]] < self.pr[x]:
                        self.swap(i, left)
                        i = left
                        left = 2*i+1
                        right = left+1
                    else:
                        return
                else:
                    if self.pr[self.arr[right]] < self.pr[x]:
                        self.swap(i, right)
                        i = right
                        left = 2*i+1
                        right = left+1
                    else:
                        return

    def add(self, ki, priority):
        self.arr.append(ki)
        try:
            self.pm[ki] = self.size
            self.pr[ki] = priority
        except KeyError:
            for _ in range(ki - self.size):
                self.pm.append(None)
                self.pr.append(None)
            self.pm.append(self.size)
            self.pr.append(priority)
        self.size += 1
        self.bubbleup(self.size-1)

    def remove(self, ki):
        try:
            position = self.pm[ki]
        except KeyError:
            print('element {} not found'.format(ki))
            return
        if position is not None:
            self.swap(position, self.size-1)
            del self.arr[-1]
            self.size -= 1
            self.pm[ki] = None
            self.bubbleup(position)
            self.bubbledown(position)
            print('element {} removed successfully'.format(ki))
        else:
            print('element {} not found'.format(ki))

    def poll(self):
        if self.size == 0:
            return 'IPQ is empty'
        if self.size == 1:
            self.size = 0
            ki = self.arr.pop()
            self.pm[ki] = None
            return ki
        x = self.arr[0]
        y = self.arr.pop()
        self.arr[0] = y
        self.size -= 1
        self.pm[x] = None
        self.pm[y] = 0
        self.bubbledown(0)
        return x

    def construct(self, a, b):
        self.arr = list(a)
        self.size = len(a)
        m = max(a)
        self.pm = [None]*(m + 1)
        self.pr = [None]*(m + 1)
        for i in range(self.size):
            self.pm[a[i]] = i
            self.pr[a[i]] = b[i]
        for i in range((self.size-2)//2, -1, -1):
            self.bubbledown(i)


priority = [11, 2, 4, 8, 1, 6, 7, 9]
keys = [0, 1, 2, 3, 4, 5, 6, 7]
myPQ = indexedPQ()
myPQ.construct(priority, keys)
myPQ.remove(2)
myPQ.add(11, 1)
for _ in range(8):
    print(myPQ.poll())
print(myPQ.arr)
print(myPQ.remove(6), myPQ.size)
