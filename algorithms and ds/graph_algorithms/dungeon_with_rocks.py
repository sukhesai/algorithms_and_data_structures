from collections import deque


def solve(sr, sc, visited, R, C, path):
    r_queue = deque()
    c_queue = deque()
    r_queue.append(sr)
    c_queue.append(sc)
    visited[C*sr+sc] = True
    r_dirs = (-1, 1, 0, 0)
    c_dirs = (0, 0, 1, -1)
    steps = 0
    nodes_in_next_level = 0
    nodes_left_in_current_level = 1
    while r_queue:
        cr = r_queue.popleft()
        cc = c_queue.popleft()
        print('current row, column: {},{}'.format(cr, cc))
        print('current step:', steps)
        if data[cr*C+cc] == '#':
            return steps, path

        for i in range(4):
            nr = cr + r_dirs[i]
            nc = cc + c_dirs[i]
            if nr >= R or nc >= C or not data[nr*C+nc] or visited[nr*C+nc] or nr < 0 or nc < 0:
                continue
            nodes_in_next_level += 1
            print('its neighbour\'s row,column: {},{}'.format(nr, nc))
            r_queue.append(nr)
            c_queue.append(nc)
            visited[nr*C+nc] = True
            path[nr*C+nc] = cr*C + cc

        nodes_left_in_current_level -= 1
        if nodes_left_in_current_level == 0:
            nodes_left_in_current_level = nodes_in_next_level
            nodes_in_next_level = 0
            steps += 1
        print('steps after visiting its all neighbours:', steps)
    return steps, path

data = (True, True, False, False, True, False, True, True, False, True, True, False, True, True, '#')
R = 3
C = 5
visited = [False]*len(data)
path = [None]*len(data)
print(solve(0, 0, visited, R, C, path))
