from collections import deque


class heap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def bubbleup(self, i):
        parent = (i-1) >> 2
        x = self.arr[i]
        while i > 0 and x < self.arr[parent]:
            self.arr[i] = self.arr[parent]
            i = parent
            parent = (i-1) >> 2
        self.arr[i] = x

    def bubbledown(self, i):
        left = (i << 1) + 1
        right = left + 1
        while left < self.size:
            smallest = i
            if self.arr[left] < self.arr[i]:
                smallest = left
            if right < self.size and self.arr[right] < self.arr[smallest]:
                smallest = right
            if smallest is not i:
                self.swap(smallest, i)
                i = smallest
                left = (i << 1) + 1
                right = left + 1
            else:
                return

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    def add(self, x):
        self.arr.append(x)
        self.bubbleup(self.size)
        self.size += 1

    def remove(self, x):
        position = self.find(x)
        if position is not False:
            self.arr[position] = self.arr.pop()
            self.size -= 1
            self.bubbleup(position)
            self.bubbledown(position)
            return "successfully removed {}".format(x)
        else:
            return "element({}) not found in PQ".format(x)

    def find(self, x):
        if self.size == 0:
            return False
        queue = deque()
        queue.append(0)
        while queue:
            temp = queue.popleft()
            if self.arr[temp] == x:
                return temp
            if self.arr[temp] < x:
                if 2*temp + 2 < self.size:
                    queue.append(2*temp+1)
                    queue.append(2*temp+2)
                elif 2*temp+1 < self.size:
                    queue.append(2*temp+1)
        return False

    def poll(self):
        if self.size == 1:
            self.size = 0
            return self.arr.pop()
        x = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.size -= 1
        self.bubbledown(0)
        return x

    def construct(self, a):
        self.arr = list(a)
        self.size = len(a)
        for i in range((self.size - 2) // 2, -1, -1):
            self.bubbledown(i)


a=[6,2,4,8,1,6,7,2]
myPQ=heap()
myPQ.construct(a)
print(myPQ.arr)
print(myPQ.remove(6),myPQ.size)
myPQ.add(1.5)
for i in range(myPQ.size):
    print(myPQ.poll())