n=int(input())
arr=list(map(int, input().split()))
a=arr[n-1]
b=n-2
for i in range(n):
    if a <arr[b] and b>=0:
        arr[n-1-i]=arr[b]
        b-=1
        # Make iteration to give the same output value
        for i in arr:print(i,end=" ")
        print("")
    else:
        arr[n-i-1]=a
        for i in arr:print(i,end=" ")
        print("")
        break