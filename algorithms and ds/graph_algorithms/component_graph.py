

def counting_sort(a):
    c = [0]*(n+1)
    for i in range(n):
        c[a[i][0]] += 1
    for i in range(1, n):
        c[i] += c[i-1]
    b = [None]*n
    for i in range(n-1, -1, -1):
        b[c[a[i][0]]-1] = a[i]
        c[a[i][0]] -= 1
    return b


def dfs(i, next_id, low, ids, onstack, stack):
    ids[i] = next_id
    low[i] = next_id
    next_id += 1
    onstack[i] = True
    stack.append(i)
    for neighbour in g[i]:
        if ids[neighbour] is None:
            next_id = dfs(neighbour, next_id, low, ids, onstack, stack)
        if onstack[neighbour]:
            low[i] = min(low[i], low[neighbour])
    if low[i] == ids[i]:
        while stack[-1] != i:
            node = stack.pop()
            low[node] = i
            onstack[node] = False
        node = stack.pop()
        low[node] = i
        onstack[node] = False
    return next_id


def strongly_connected_components():
    next_id = 0
    low = [None]*n
    ids = [None]*n
    onstack = [False]*n
    for i in range(n):
        if ids[i] is None:
            stack = []
            next_id = dfs(i, next_id, low, ids, onstack, stack)
    make_component_graph(low)


def make_component_graph(low):
    for i, v in enumerate(low):
        low[i] = (v, i)
    low = counting_sort(low)
    sccs = []
    new_vertices = [0]
    new_scc = True
    print(low)
    for i in range(1, n):
        if low[i][0] == low[i-1][0]:
            if new_scc:
                sccs.append([low[i-1][1], low[i][1]])
                new_scc = False
            else:
                sccs[-1].append(low[i][1])
        else:
            new_scc = True
            new_vertices.append(low[i][1])
    print(sccs)
    print(new_vertices)


g = [[1], [2, 3], [3, 5], [4, 7], [], [6, 9], [2], [3, 8], [], []]
n = 10
strongly_connected_components()
