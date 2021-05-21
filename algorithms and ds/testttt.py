
def solve(tree, color):
    def merge(s1,s2):
        print(f'merge {s1} and {s2}')
        if len(s1)>len(s2):
            s1,s2=s2,s1
        print(f'returning {s2.union(s1)}')
        return s2.union(s1)
    def contains(s1,s2):
        if len(s1)>len(s2):
            s1,s2 = s2,s1
        for i in s1:
            if i in s2:
                return True
        return False
    def dfs(i, p):
        print(f'enter {i} {p}')
        col = {color[i]}
        for nbr in tree[i]:
            if nbr != p:
                y = dfs(nbr, i)
                if col and y:
                    if contains(col,y):
                        col = set()
                    else:
                        col = merge(y,col)
        if col:
            ans[0] += 1
        print(f'returned {i} {p} with set {col}')
        return col
    ans = [0]
    dfs(0,0)
    return ans[0]



tree = [
    [1],
    [0, 3, 2],
    [1],
    [1]
]
color = [0, 0, 0, 3]
print(solve(tree,color))
            