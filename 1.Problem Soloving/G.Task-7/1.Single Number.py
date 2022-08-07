import sys,math
def solve(nums):
    from collections import Counter
    l=Counter(nums).most_common()
    # print(l)
    for i in range(len(l)):
        if l[i][1]==1:
            print(l[i][0])
            break
nums=list(map(int,sys.stdin.readline().split()))
solve(nums)