# My solution for sorting
# using built in method 
arr=list(map(int, input().split()))
arr.sort()
for i in arr:
    print(i,end=' ')
print('')
# Second using swaping 
arr=list(map(int, input().split()))
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if arr[j]<arr[i] and i!=j:
            swap=arr[j]
            arr[j]=arr[i]
            arr[i]=swap
for i in arr:print(i,end=" ")

# The Correction of Codes 


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           l[j+1] = key  

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))