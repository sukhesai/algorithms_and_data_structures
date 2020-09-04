

def dfs(i, id_no):
    stack.append(i)
    onstack[i] = True
    ids[i] = id_no
    low[i] = id_no
    id_no += 1
    for neighbour in g[i]:
        if ids[neighbour] is None:
            id_no = dfs(neighbour, id_no)
        if onstack[neighbour]:
            low[i] = min(low[neighbour], low[i])
    if ids[i] == low[i]:
        while True:
            node = stack.pop()
            low[node] = i
            onstack[node] = False
            if node == i:
                break
    return id_no


g = [[1], [2, 3], [3, 5], [4, 7], [], [6, 9], [2], [3, 8], [], []]
n = 10
low = [None]*n
ids = [None]*n
onstack = [False]*n
id_no = 0
stack = []
for i in range(n):
    if ids[i] is None:
        id_no = dfs(i, id_no)
print(low)
