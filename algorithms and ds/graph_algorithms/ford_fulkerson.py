import math

def max_flow(delta):
    delta = 2**(math.floor(math.log2(delta)))
    ans = 0
    while delta > 0:
        visited = [False]*(n+2)
        visited[s] = True
        aug_val = find_aug(s, visited, delta, 2000000)
        if aug_val == 0:
            delta >>= 1
        ans += aug_val
    return ans


def find_aug(i, visited, delta, aug_val):
    if aug_val == 0:
        return 0
    if i == t:
        return aug_val
    for neighbour in g[i]:
        if not visited[neighbour[0]] and neighbour[2]-neighbour[1] >= delta:
            visited[neighbour[0]] = True
            new_aug = find_aug(neighbour[0], visited, delta, min(aug_val, neighbour[2]-neighbour[1]))
            if new_aug > 0:
                if neighbour[3]:
                    neighbour[1] += new_aug
                    rev_path[(i,neighbour[0])][1] -= new_aug
                return new_aug
    return 0


def insert(i, j, cap):
    g[i].append([j,0,cap, True])
    g[j].append([i,0,0, False])
    rev_path[(i,j)] = g[j][-1]
    rev_path[(j,i)] = g[i][-1]


entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # 0: source
  [0, 0, 5, 2, 0, 0],  # 1: source
  [0, 0, 0, 0, 4, 4],  # 2: Intermediate node
  [0, 0, 0, 0, 6, 6],  # 3: Intermediate node
  [0, 0, 0, 0, 0, 0],  # 4: sink
  [0, 0, 0, 0, 0, 0],  # 5: sink
]
n = len(path)
g = [[] for _ in range(n+2)]
rev_path = dict()
s = n
t = n+1
delta = 0
for row in range(n):
    for column in range(n):
        if path[row][column] != 0:
            insert(row,column,path[row][column])
            delta = max(delta, path[row][column])
for entry in entrances:
    insert(s,entry,sum(path[entry]))
    delta = max(delta, g[s][-1][2])
for ext in exits:
    insert(ext,t,sum(path[i][ext] for i in range(n)))
    delta = max(delta, g[ext][-1][2])
print(max_flow(delta))
