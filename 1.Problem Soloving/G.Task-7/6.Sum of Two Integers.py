def solve(a,b):
    return a+b

def solve2(a,b):
    a=min(a,b)
    b=max(a,b)
    while b!=0:
        temp =(a&b)<<1
        a=a^b
        b=temp
    return a


import sys,math
a,b=map(int,sys.stdin.readline().split())
print(solve(a,b))
print(solve2(a,b))