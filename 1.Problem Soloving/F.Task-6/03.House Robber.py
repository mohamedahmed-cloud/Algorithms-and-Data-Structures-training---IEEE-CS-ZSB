def solve(nums):
    n=len(nums)
    if n>3:
        nums[2]+=nums[0]
        for i in range(3,n):
            nums[i]+=max(nums[i-2],nums[i-3])
        return max(nums[-2],nums[-1])
    else:
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        if n==3:
            return max(nums[0]+nums[2],nums[1])



import sys,math
nums=list(map(int,sys.stdin.readline().split()))
print(solve(nums))