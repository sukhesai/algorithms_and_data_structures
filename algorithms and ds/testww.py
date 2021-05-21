from collections import deque


def makeGraph(data,g):
    for i in range(r-1):
        for j in range(c-1):
            if data[i][j] == data[i][j+1]:
                g[i*c+j].append((i,j+1))
                g[i*c+j+1].append((i,j))
            if data[i][j] == data[i+1][j]:
                g[i*c+j].append((i+1,j))
                g[(i+1)*c+j].append((i,j))
    for i in range(r-1):
        if data[i][c-1] == data[i+1][c-1]:
            g[i*c+c-1].append((i+1,c-1))
            g[(i+1)*c+c-1].append((i,c-1))
    for j in range(c-1):
        if data[r-1][j] == data[r-1][j+1]:
            g[(r-1)*c+j].append((r-1,j+1))
            g[(r-1)*c+j+1].append((r-1,j))


def get_remaining():
    remtype = set()
    rem = set()
    for i in range(c):
        if pakka[row*c+i] or data[row][i] in remtype:
            continue
        rem.add(row*c+i)
        remtype.add(data[row][i])
    return rem


def makePakka(cord, visited):
    q = deque()
    q.append(cord)
    visited[cord] = True
    result = True
    while q:
        p = q.popleft()
        if pakka[p] or p//c == r-1 or data[p//c][p%c] == data[(p//c)-1][p%c]:
            for i in g[p]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        else:
            result = False
            break
    return result


t = int(input())
for tt in range(1,t+1):
    r,c=map(int,input().split())
    data = [None]*r
    for row in range(r):
        data[row] = input()
    g = [[]]*(r*c)
    makeGraph(data,g)
    pakka = [False]*(r*c)
    row = r-1
    ans = ''
    while row > 0:
        remaining = get_remaining()
        flag = True
        while remaining:
            flag = False
            for i in remaining:
                visited = list(pakka)
                if makePakka(i, visited):
                    ans = i + ans
                    remaining.remove(i)
                    flag = True
                    break
            if not flag:
                break
        if not flag:
            break
        row -= 1
    if not flag:
        ans = "-1"
    print(f'Case #{tt}: {ans}')
    


