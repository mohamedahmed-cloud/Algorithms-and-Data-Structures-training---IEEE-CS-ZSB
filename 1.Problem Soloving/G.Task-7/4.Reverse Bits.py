def solve(n):
    s=bin(n)[2:]
    s=f"{s}"
    s=s[::-1]
    a=len(s)
    if a<32:
        s+="0"*(32-a)
    return int(s,2)



import sys
n=int(sys.stdin.readline(),2)
print(solve(n))
