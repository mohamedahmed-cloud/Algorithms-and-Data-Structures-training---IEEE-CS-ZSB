# Input Operation
n = int(input())
list1 = []
list1 = list(map(int, input().split()))
# Output Operation
max1 = 0
for i in list1:
    if i >= max1:
        max1 = i
list1.remove(max1)
max2 = 0
for i in list1:
    if i >= max2:
        max2 = i
print(max1*max2)
