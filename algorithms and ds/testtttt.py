def solution(s):
    def binary_search(x): # returns index of leftmost qn which is greater than x
        l,r=0,len(pq_arr)-1
        while l!=r:
            m = (l+r)//2
            if pq_arr[m][1] <= x:
                l = m+1
            else:
                r = m
        return l
    s = int(s)
    pq_arr = [(0,1),(1,2)]  # this is list of (pn,qn) where pn/qn is nth convergent of continued fraction of root(2)-1
    i = 1
    while pq_arr[i][1] <= s:
        pq_arr.append((2*pq_arr[i][0]+pq_arr[i-1][0],2*pq_arr[i][1]+pq_arr[i-1][1]))
        i += 1
    ans = (s*(s+1))//2
    while s > 0:
        i = binary_search(s)
        x = 1 if i%2 == 1 else -1
        b, k = s//pq_arr[i-1][1], s%pq_arr[i-1][1]
        ans += ((b*(b*pq_arr[i-1][0]*pq_arr[i-1][1]+pq_arr[i-1][0]-pq_arr[i-1][1]+x))//2)
        ans += (k*b*pq_arr[i-1][0])
        s = k
    return str(ans)

print(solution('77'))