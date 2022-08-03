def solve(s):
    ans=len(s)
    # strring=""
    n=len(s)
    # print(n,s)
    for i in range(n):
        l,r=i,i
        while l>=0 and r< n and s[l]==s[r]:
            if abs(r-l)>0:
                # print(i,l,r)
                ans+=1
            r+=1
            l-=1
        l,r=i,i+1
        while l>=0 and r<n and s[l]==s[r]:
            if abs(r-l)>0 :
                ans+=1
            r+=1
            l-=1
    return ans





import sys,math
s=sys.stdin.readline()
s=s[:-1]
print(solve(s))