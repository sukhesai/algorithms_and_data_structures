

def suffix_array(a):
    n, l = len(a), 0
    sa = [[a[i],i] for i in range(n)]
    pos_map = [None]*n
    while l < n:
        sa.sort(key=lambda x: x[0])
        rank, last = 0, sa[0][0]
        for i in range(n):
            pos_map[sa[i][1]] = i
            if sa[i][0] != last:
                rank += 1
                last = sa[i][0]
            sa[i][0] = rank
        new_tuple = [(sa[i][0], sa[pos_map[sa[i][1]+l]][0] if sa[i][1]+l < n else -1) for i in range(n)]
        sa = [[new_tuple[i],sa[i][1]] for i in range(n)]
        l = 1 if not l else l << 1
    return [sa[i][1] for i in range(n)]


def lcp_array():
    lcp = [0]*n
    rank = ranklist[numbr_iter]
    k = 0
    for i in range(n):
        if k != 0:
            k -= 1
        if rank[i] != 0:
            j = SA[rank[i]-1]
            while i + k < n and j + k < n and a[i + k] == a[j + k]:
                k += 1
            lcp[rank[i]] = k
    return lcp


SA, ranklist = suffix_array(a)
LCP = lcp_array()
print(LCP)
