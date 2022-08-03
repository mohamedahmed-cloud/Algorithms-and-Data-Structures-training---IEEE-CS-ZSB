def solve(nums):
    n=len(nums)
    if n>3:
        arr1=nums[1:]
        arr2=nums[:-1]
        arr1[2]+=arr1[0]
        arr2[2]+=arr2[0]
        for i in range(3,n-1):
            arr1[i]+=max(arr1[i-2],arr1[i-3])
        for i in range(3,n-1):
            arr2[i]+=max(arr2[i-2],arr2[i-3])
        max1=max(arr1[-1],arr1[-2])
        max2=max(arr2[-1],arr2[-2])
        return max(max1,max2)
    else:
        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        if n==3:
            x=max(nums[0]+nums[2])
            return max(x,nums[1])





import sys,math
nums=[int(x) for x in sys.stdin.readline().split()]
print(solve(nums))