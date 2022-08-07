def solve(nums):
    n=len(nums)
    for i in range(n+1):
        if i not in nums:
            return i

def solve2(nums):
    # faster than 90.02% of Python3 online submissions for Missing Number.
    a=len(nums)
    s=sum(nums)
    all=a*(a+1)/2
    return int(all-s)
def solve3(nums):
    ans=len(nums)
    for i in range(ans):
        ans+=i-nums[i]
    return ans
import sys,math
nums =list(map(int,sys.stdin.readline().split()))
# first solution
print(solve(nums))
# second one
print(solve2(nums))
# thrid one
print(solve3(nums))
