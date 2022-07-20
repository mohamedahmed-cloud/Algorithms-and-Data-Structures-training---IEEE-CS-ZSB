from collections import Counter
import sys
def Majority(arr,n):
    a=Counter(arr)
    b=a.most_common()
    for i in range(len(b)):
        if b[i][1]>n/2:
            return 1
    return 0
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
print(Majority(arr,n))