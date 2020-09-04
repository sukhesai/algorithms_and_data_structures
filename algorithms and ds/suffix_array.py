import math
a = 'banana'
n = len(a)
numbr_iter = math.ceil(math.log2(n))

def suffix_array(a):
    rnklst = [[None]*n]*(numbr_iter + 1)
    rnklst[0] = [ord(a[i]) - ord('a') for i in range(n)]
    step = 1
    offset = 1
    while step <= numbr_iter:
        L = [None]*n
        for i in range(n):
            try:
                L[i] = [(rnklst[step - 1][i], rnklst[step - 1][i + offset]), i]
            except IndexError:
                L[i] = [(rnklst[step - 1][i], -1), i]
        L.sort()
        pr_rank = L[0][0]
        L[0][0] = 0
        rank = 0
        for i in range(1, n):
            if pr_rank != L[i][0]:
                rank += 1
            pr_rank = L[i][0]
            L[i][0] = rank
        for i in range(n):
            rnklst[step][L[i][1]] = L[i][0]
        step += 1
        offset *= 2
    SA = [None]*n
    for i in range(n):
        SA[rnklst[numbr_iter][i]] = i
    return SA, rnklst


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
