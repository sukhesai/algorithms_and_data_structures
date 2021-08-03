import math

nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
M = [0]*len(nums)
P = [0]*len(nums)
hi = 0
for i in range(1, len(nums)):
    if nums[i] <= nums[M[0]]:
        M[0] = i
    elif nums[i] > nums[M[hi]]:
        hi += 1
        M[hi] = i
        P[i] = M[hi-1]
    else:
        lo, hii = 0, hi
        while hii > lo:
            mid = math.ceil((hii+lo)/2)
            if nums[M[mid]] >= nums[i]:
                hii = mid -1
            else:
                lo = mid
        M[lo+1] = i
        P[i] = M[lo]

print(hi+1,M[hi],P)
