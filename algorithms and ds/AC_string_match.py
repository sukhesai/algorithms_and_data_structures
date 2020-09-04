from collections import deque


class node:
    def __init__(self):
        self.children = {}
        self.suffixlink = None
        self.wordid = None
        self.endwordlink = None
        self.parent = None
        self.char = None
        self.isleaf = False


class Aho:
    def __init__(self):
        self.trie = [node()]

    def get_size(self):
        return len(self.trie)

    def insert_pattern(self, P, wordid):
        curr = 0
        for i in P:
            if i in self.trie[curr].children:
                curr = self.trie[curr].children[i]
            else:
                new = node()
                new.parent = curr
                new.char = i
                self.trie[curr].children[i] = self.get_size()
                self.trie.append(new)
                curr = self.get_size()-1
        self.trie[curr].isleaf = True
        self.trie[curr].wordid = wordid

    def prepare_aho(self):
        curr = 0
        dq = deque()
        dq.append(curr)
        while dq:
            this = dq.popleft()
            if this == 0:
                self.trie[this].suffixlink = 0
                self.trie[this].endwordlink = 0
            elif self.trie[this].parent == 0:
                self.trie[this].suffixlink = 0
                self.trie[this].endwordlink = 0
            else:
                char = self.trie[this].char
                parentsuffix = self.trie[self.trie[this].parent].suffixlink
                while True:
                    if char in self.trie[parentsuffix].children:
                        self.trie[this].suffixlink = self.trie[parentsuffix].children[char]
                        break
                    if parentsuffix == 0:
                        self.trie[this].suffixlink = 0
                        break
                    parentsuffix = self.trie[parentsuffix].suffixlink
                if self.trie[this].isleaf:
                    self.trie[this].endwordlink = this
                else:
                    self.trie[this].endwordlink = self.trie[self.trie[this].suffixlink].endwordlink
            for _, v in self.trie[this].children.items():
                dq.append(v)

    def search(self, T):
        n = len(T)
        curr = 0
        for i in range(n):
            while True:
                if T[i] in self.trie[curr].children:
                    curr = self.trie[curr].children[T[i]]
                    break
                if curr == 0:
                    break
                curr = self.trie[curr].suffixlink
            check = curr
            while True:
                check = self.trie[check].endwordlink
                if check == 0:
                    break
                wrdid = self.trie[check].wordid
                print('match found {} at shiftend {}'.format(wrdid, i))
                check = self.trie[check].suffixlink


ac = Aho()
patterns = ['aba', 'aaba', 'baba', 'baab']
for i, P in enumerate(patterns):
    ac.insert_pattern(P, i)
ac.prepare_aho()
ac.search('ababbababaab')
