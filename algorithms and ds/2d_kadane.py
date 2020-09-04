#code
import math


def kadane(t, n):
    msum = t[0]
    sumi = msum
    for i in range(1,n):
        if sumi < 0:
            sumi = t[i]
        else:
            sumi += t[i]
        msum = max(msum, sumi)
    return msum


if __name__ == '__main__':
    
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().split())
        a = list(map(int, input().split()))
        print(len(a))
        msum = -math.inf
        for i in range(r):
            temp = [0]*c
            for j in range(i,r):
                for k in range(c):
                    print(j,c,k)
                    temp[k] += a[(j*c)+k]
                msum = max(msum, kadane(temp, c))
        print(msum)
