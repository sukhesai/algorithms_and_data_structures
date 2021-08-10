import math


a = [0,5,2,5,4,3,1,6,3]
l = len(a)
dp = [[i] for i in a]
j = 1
while 2**j <= l:
    i = 0
    while i+2**j <= l:
        dp[i].append(min(dp[i][j-1],dp[i+2**(j-1)][j-1]))
        i += 1
    j += 1

def findmin(l,r):
    j=math.floor(math.log2(r-l+1))
    return min(dp[l][j],dp[r-2**j+1][j])

for i in range(2):
    for j in range(i,l):
        print(findmin(i,j))
