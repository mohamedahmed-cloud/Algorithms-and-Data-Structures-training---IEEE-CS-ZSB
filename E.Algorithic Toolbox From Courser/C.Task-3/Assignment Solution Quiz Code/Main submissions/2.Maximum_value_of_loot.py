# Input Operation
n,capacity=list(map(int,input().split()))
arr = []
if capacity==0:
    print(0)
    quit()
for i in range(n):
    V,M=list(map(int,input().split()))
    # print(V,M)
    # Ouput Operation
    if V==0:
        continue
    arr.append((V,M))
# Sorting Arr According to Value => Key

arr.sort( key=lambda x:x[0]/x[1],reverse=True)
out=0
for v,m in arr:
    if capacity==0:
        break
    can_take=min(capacity,m)
    out+=can_take*(v/m)
    capacity-=can_take
print(out)