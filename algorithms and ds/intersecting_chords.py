C = []
total_no = len(C)
P = []
for i in range(total_no):
    P.append((C[i][0], i))
    P.append((C[i][1], i))
P.sort()
pos = [-1]*total_no
count = 0
pattern = []
for i in range(2*total_no):
    x = P[i][1]
    if pos[x] == -1:
        pos[x] = count
        pattern.append(count)
        count += 1
    else:
        pattern.append(pos[x])

seen = [0]*total_no
first_endpoints = [0]*total_no
open_intervals = []                    # here open_interval is a list. implement it as a order_stastic_tree.
intersections = 0
for i in range(2*total_no):
    x = pattern[i]
    if seen[x] == 0:
        first_endpoints[x] = i
        seen[x] = 1
        open_intervals.append(i)
    else:
        y = first_endpoints[x]
        for j in open_intervals:
            if j > y:
                intersections += 1
        open_intervals.remove(y)
print(intersections)
