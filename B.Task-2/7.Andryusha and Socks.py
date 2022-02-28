# input operation
n=int(input())
order_of_pulling=list(map(int,input().split()))
i=0
exist=1
list=[]
while i <n:
    list.append(exist)
    if order_of_pulling[i]!=order_of_pulling[i+1]:
        exist+=1
        list.append(exist)
    
    if order_of_pulling[i]==order_of_pulling[i+1]:
        exist-=1
        list.append(exist)

    i+=1
print(max(list))