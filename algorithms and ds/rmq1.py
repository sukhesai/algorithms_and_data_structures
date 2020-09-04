import math

b=[0,1,2,3,4,5,6,7,8]
a=[0,5,2,5,4,3,1,6,3]
l=len(a)
dp=[[] for i in range(l)]
for i in range(l):
    dp[i].append(a[i])
    minlast=a[i]
    j=1
    while i+2**j-1<l:
        print(i,j,i+2**(j-1),i+2**j)
        minlast=min(minlast,*a[i+2**(j-1):i+2**j])
        dp[i].append(minlast)
        j+=1

def findmin(l,r):
    j=math.floor(math.log2(r-l+1))
    return min(dp[l][j],dp[r-2**j+1][j])

for i in range(l):
    for j in range(i,l):
        print(i,j,findmin(i,j))
