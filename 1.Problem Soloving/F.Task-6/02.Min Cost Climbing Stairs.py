def solve(cost):
    n=len(cost)
    for i in range(n-3,-1,-1):
        cost[i]+=min(cost[i+1],cost[i+2])

    return min(cost[0],cost[1])
import sys

cost=list(map(int,sys.stdin.readline().split()))
print(solve(cost))