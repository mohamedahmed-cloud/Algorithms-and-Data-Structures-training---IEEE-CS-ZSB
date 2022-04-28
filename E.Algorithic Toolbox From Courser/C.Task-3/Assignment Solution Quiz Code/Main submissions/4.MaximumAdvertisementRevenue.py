n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
out=0
for i in range(n):
    max1=max(arr1)
    max2=max(arr2)
    # print(max1,max2)
    out+=max1*max2
    arr1.remove(max1)
    arr2.remove(max2)

print(out)