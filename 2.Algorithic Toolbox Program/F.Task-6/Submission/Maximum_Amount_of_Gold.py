def knapsack(W,N,Warr):
    check=[[0 for x in range(W+1)] for y in range(N+1)]
    for i in range(N+1):
        for j in range(W+1):
            if i==0 or j==0:
                check[i][j]==0
            elif Warr[i-1]<=j:
                check[i][j]=max(Warr[i-1]+ check[i-1][j-Warr[i-1]],check[i-1][j])
            else:
                check[i][j] = check[i-1][j]
    return check[N][W]


import sys,math
W,N=map(int,sys.stdin.readline().split())
Warr=list(map(int,sys.stdin.readline().split()))
print(knapsack(W,N,Warr))