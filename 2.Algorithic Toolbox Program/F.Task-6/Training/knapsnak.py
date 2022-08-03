# Naive Algorithm
def solve(w,v,n,c):
    if n==0 or c==0:
        return 0
    elif w[n-1]>c:
        return solve(w,v,n-1,c)
    else:
        temp1=solve(w,v,n-1,c)
        temp2=v[n-1]+solve(w,v,n-1,c-w[n-1])
        return max(temp1,temp2)
n,c= map(int, input().split())
w=list(map(int, input().split()))
v=list(map(int, input().split()))
a=solve(w,c,n,c)
print(a)