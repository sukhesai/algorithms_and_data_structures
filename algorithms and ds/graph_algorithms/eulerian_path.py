
def calc_in_out():
    for node in range(n):
        for edge in g[node]:
            Out[node] += 1
            In[edge] += 1


def eulerian_path_exist():
    start_node = 0
    start_count = 0
    end_count = 0
    for i in range(n):
        if In[i] - Out[i] > 1 or In[i] - Out[i] < -1:
            return False
        if In[i] - Out[i] == 1:
            end_count += 1
        if In[i] - Out[i] == -1:
            start_node = i
            start_count += 1
    if (end_count == 0 and start_count == 0) or (start_count == 1 and end_count == 1):
        return start_node
    else:
        return False


def get_eulerian_path(start_node):
    dfs(start_node)


def dfs(i):
    while Out[i] > 0:
        Out[i] -= 1
        dfs(g[i][Out[i]])
    path.append(i)


g = [[], [2, 3], [2, 4, 4], [1, 2, 5], [3, 6], [6], [3]]
n = len(g)
m = 7
path = []
In = [0]*n
Out = [0]*n
calc_in_out()
path_exist = eulerian_path_exist()
print(path_exist)
get_eulerian_path(path_exist)
print(path)
print(In, Out)
