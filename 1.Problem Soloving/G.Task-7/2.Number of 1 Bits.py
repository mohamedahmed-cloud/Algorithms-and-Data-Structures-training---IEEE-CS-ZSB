def solve(n):
    # Very Important Notes Take binary from user int(input(),2)
    count=0
    while n:
        count+=n%2
        n=n>>1
    return count
    # another solution
def solve2(n):
    a=bin(n)[2:]
    s=str(a)
    return s.count("1")

def solve3(n):
    count=0
    while n:
        n&=n-1
        count+=1
    return count

import sys,math
n=int(input(),2)
# First
print(solve(n))
# Second
print(solve2(n))
# Thrid 
print(solve3(n))