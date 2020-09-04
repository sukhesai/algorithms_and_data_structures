def dfs(at, visited):
    if visited[at]:
        return
    visited[at] = True
    print(at)
    for neighbour in g[at]:  # using adjecency list
        dfs(neighbour, visited)


def dfs_iterative(at, visited):
    stack = [at]
    visited[at] = True
    while stack:
        current = stack.pop()
        print("inside dfs {}".format(current))
        for next_vertex in g[current]:
            if not visited[next_vertex]:
                stack.append(next_vertex)
                visited[next_vertex] = True


def get_no_of_components(n, visited):
    count = 0
    for i in range(n):
        print(i, count, visited[i])
        if visited[i]:
            continue
        dfs_iterative(i, visited)
        count += 1
    print("no of connected components:{}".format(count))


g = ((), (2, ), (1, ), (4, 5), (3, 5), (4, 3))
for i in g:
    print(i)
    for j in i:
        print(j)
visited = [False]*len(g)
# dfs(0, visited)
visited = [False]*len(g)
# dfs_iterative(0, visited)
visited = [False]*len(g)
get_no_of_components(len(g), visited)
