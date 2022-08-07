def solve(n):
    ans=[]
    for i in range(n+1):
        ans.append(str(bin(i)[2:]).count("1"))
    return ans

def solve2(n):
    ans=[]
    for i in range(n+1):
        count=0
        while i!=0:
            count+=i%2
            i=i//2
        ans.append(count)
    return ans

import sys,math
n=int(sys.stdin.readline())
# First Solution 
print(solve(n))
# Second solution 
print(solve2(n))
