import sys
import io,os
a=int(sys.stdin.readline())
arr1=arr = [int(x) for x in sys.stdin.readline().split()]
b=int(sys.stdin.readline())
arr2=[int(x) for x in sys.stdin.readline().split()]
for i in arr2:
    if i in arr1:
        sys.stdout.write(str(arr1.index(i))+" ")
        # print(arr1.index(i),end=" ")
    else:
        sys.stdout.write(str(-1)+" ")

