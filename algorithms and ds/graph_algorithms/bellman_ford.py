import math


def bellman_ford(a):
    distance = [math.inf]*V
    path = [None]*V
    distance[a] = 0
    for _ in range(V-1):
        for edge in edgelist:
            if distance[edge[0]] + edge[2] < distance[edge[1]]:
                distance[edge[1]] = distance[edge[0]] + edge[2]
                path[edge[1]] = edge[0]

    for _ in range(V-1):
        for edge in edgelist:
            if distance[edge[0]] + edge[2] < distance[edge[1]]:
                distance[edge[1]] = -math.inf
                path[edge[1]] = -1

    return distance, path


g = (((1,5),),((2,20),(5,30),(6,60)),((3,10),(4,75)),((2,-15),),((9,100),),((4,25),(6,5),(8,50)),((7,-50),),((8,-10),),(),())
edgelist = []
for num, i in enumerate(g):
    print(num, i)
    for j in i:
        edgelist.append((num, j[0], j[1]))
print(edgelist)
V = len(g)
print(bellman_ford(0))
