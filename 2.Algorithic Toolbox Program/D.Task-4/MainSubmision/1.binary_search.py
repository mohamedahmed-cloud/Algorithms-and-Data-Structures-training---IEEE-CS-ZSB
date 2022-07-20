import sys
def binary_search(arr,l,h,key):
        while(l<=h):
            mid=(l+h)//2
            if arr[mid]==key:
                return mid
            if arr[mid]>key:
                h=mid-1
            else :
                l=mid+1
        return -1 
n1=int(sys.stdin.readline())
arr1=[int(x) for x in sys.stdin.readline().split()]
n2=int(sys.stdin.readline())
arr2=[int(x) for x in sys.stdin.readline().split()]
l,r=0,n1-1
for key in arr2:
    a=binary_search(arr1,l,r,key)
    sys.stdout.write(str(a)+" ")

    