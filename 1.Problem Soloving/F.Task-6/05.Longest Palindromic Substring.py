def solve(s):
    # Time Limti 
    # s+="+"
    # n=len(s)
    # length=0
    # ans=""
    # for i in range(n):
    #     for j in range(i,n):
    #         check=s[i:j]
    #         if check==check[::-1]:
    #             if j-i+1>length:
    #                 length=j-i+1
    #                 ans=check
    # return ans
    
    # Another Solution 
    ans=""
    anslen=0
    n=len(s)
    for i in range(n):
        # check for odd 
        l,r=i,i
        while l>=0 and r<n and s[l]==s[r]:
            if r-l+1>anslen:
                ans=s[l:r+1]
                anslen=r-l+1
            r+=1
            l-=1
        # check for even 
        l,r=i,i+1
        while l>=0 and r<n and s[l]==s[r]:
            if r-l+1>anslen:
                ans=s[l:r+1]
                anslen=r-l+1
            r+=1
            l-=1
    return ans

import sys
s=sys.stdin.readline()
s=s[:-1]
print(solve(s))