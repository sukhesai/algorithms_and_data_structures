class grp:
    def __init__(self):
        self.next = None
        self.prev = None
        self.number = None
        self.representative = None


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


E = None
s = [4, 8, E, 3, E, 9, 2, 6, E, E, E, 1, 7, E, 5]
n = 10  # 0 to 9 (may need to append dummy number 0 in s)
uf = union_find()
uf.construct(n)
key_to_grp_map = dict()
grp_num = 1
curr_grp = grp()
last_elem_in_grp = None
for i in range(1, len(s)):
    if s[i] and s[i-1]:
        last_elem_in_grp = s[i]
        uf.union(s[i], s[i-1])
    elif not s[i]:
        if s[i-1]:
            represtative = uf.find(last_elem_in_grp)
            curr_grp.representative = represtative
            key_to_grp_map[represtative] = curr_grp
        curr_grp.number = grp_num
        last_group = curr_grp
        curr_grp = grp()
        last_group.next = curr_grp
        curr_grp.prev = last_group
        grp_num += 1
    else:  # s[i] is first elem in grp
        last_elem_in_grp = s[i]
curr_grp.number = grp_num
curr_grp.representative = uf.find(last_elem_in_grp)
key_to_grp_map[curr_grp.representative] = curr_grp

curr_grp = key_to_grp_map[uf.find(s[0])]
while curr_grp:
    print('grp_no:{} grp_repr:{}'.format(curr_grp.number, curr_grp.representative))
    y = curr_grp
    curr_grp = curr_grp.next
print('reverse journey:')
while y:
    print('grp_no:{} grp_repr:{}'.format(y.number, y.representative))
    y = y.prev
print("now calculating result:")
result = [None]*6
for i in range(1, n):
    group = key_to_grp_map[uf.find(i)]
    if group.number < 7:
        result[group.number-1] = i
        print(result)
        next_group = group.next
        prev_group = group.prev
        r_next = next_group.representative
        r_curr = group.representative
        if r_next:
            uf.union(r_curr, r_next)
            del key_to_grp_map[r_next]
        del key_to_grp_map[r_curr]
        n_repr = uf.find(r_curr)
        key_to_grp_map[n_repr] = next_group
        next_group.representative = n_repr
        if next_group and prev_group:
            prev_group.next = next_group
            next_group.prev = prev_group
        elif not prev_group and next_group:
            next_group.representative = n_repr
            next_group.prev = None
        print("group {} merged into {}".format(group.number, next_group.number))
print(result)
