
def search(nums, target):
    l,r=0,len(nums)-1
    while l<r:
        m = (l+r)//2
        if l == m:
            if target == nums[l]:
                return l
            else:
                return -1
        if nums[l] > nums[m]:
            if target > nums[l] or target < nums[m]:
                r = m-1
            elif target < nums[r]:
                l = m+1
            else:
                return -1
        elif nums[l] > nums[r]:
            if target > nums[l]:
                if target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif target > nums[r]:
                return -1
            else:
                l = m+1
        else:
            if target > nums[m]:
                l = m+1
            else:
                r = m
    if nums[l] == target:
        return l
    return -1
    #   0 1 2 3 4 5 6 7
nums = [8,1,2,3,4,5,6,7]
target = 6
print(search(nums,target))
