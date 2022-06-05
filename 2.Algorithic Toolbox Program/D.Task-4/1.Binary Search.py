import math
A=[1,2,3,4,5,6,7,32]
low=A[0]
high=A[-1]
key=2

def binary_search(A,low,high,key):
    iter=0
    while (low<=high) :
       
        mid=int(low+(high-low)/2)
        if key==mid:
            return A.index(mid)
        elif key<mid:
            high=mid+1
        else:
            low=mid-1
        iter+=1
        if iter>=int(math.ceil(math.log(len(A)))):
            return -1
    
out=binary_search(A,low,high,key)
print(out)