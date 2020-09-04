n, x = map(int, input().split())
i = 0
a = list(map(int, input().split()))
a.sort()
print(a)
j = n-1
pairs = 0
while i < j:
    print('start i, j:',i, j)
    if a[i]+a[j]==x:
        ii = i
        ic = 1
        while ii < j-1 and a[ii]==a[ii+1]:
            ii+=1
            ic+=1
        print('case1 ii, ic:',ii, ic)
        jj = j
        jc = 1
        print('j, jj', j, jj)
        while jj > i+1 and a[jj]==a[jj-1]:
            print('loop jj', jj)
            jc+=1
            jj-=1
        if ii >= jj:
            n = ii - jj +1
            n = n*(n+1)//2
            pairs = jc*ic - n
            
        else:
            pairs+=jc*ic
            print('case1 jj, jc, pairs:', jj, jc, pairs)
            i = ii+1
            j=jj-1
        break
    elif a[i]+a[j]<x:
        print('case2 increment i:', i+1)
        i +=1
    else:
        j-=1
        print('case3 decrement j:', j)
print(pairs)