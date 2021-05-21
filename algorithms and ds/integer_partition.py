

def get_partition(n):
    partition = {1: [[1]]}
    for i in range(2,n+1):
        ans = [[i]]
        for j in range(1,i):
            a = i-j
            for p in partition[j]:
                if p[0] <= a:
                    ans.append([a]+p)
        partition[i] = ans
    return partition[n]

print(len(get_partition(12)))