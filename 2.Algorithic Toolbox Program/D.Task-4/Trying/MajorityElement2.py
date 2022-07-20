import sys
n=int(sys.stdin.readline())
arr=[int(x) for x in sys.stdin.readline().split()]

def Majority(arr):
    for i in arr:
        if arr.count(i)>n/2:
            return 1
    return 0
print(Majority(arr))