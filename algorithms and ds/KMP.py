

def prefix_functon(P):
    m = len(P)
    pf = [None]*(m)
    pf[0] = -1
    k = -1
    for q in range(1, m):
        while k > -1 and P[k+1] != P[q]:
            k = pf[k]
        if P[k+1] == P[q]:
            k += 1
        pf[q] = k
    return pf


def KMP_search(T, P):
    m = len(P)
    n = len(T)
    pf = prefix_functon(P)
    print(pf)
    k = -1
    for i in range(n):
        while k > -1 and P[k+1] != T[i]:
            k = pf[k]
        if P[k+1] == T[i]:
            k += 1
        if k == m-1:
            print('pattern match at index:', i-m+1)
            k = pf[k]


KMP_search('ababacabababaca','ababaca')