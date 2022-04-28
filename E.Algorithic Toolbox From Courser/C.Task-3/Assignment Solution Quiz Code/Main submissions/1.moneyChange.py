# This solution by Greedy algorithm might failed with some test case so if it is failed use dynamic programming
money = int(input())
arr =[10,5,1]
# Need of it's not sorted
# sorting = sorted(arr)
# sorting.reverse()
# out = []
sum=0
for i in arr:
    while i <= money:
        # out.append(i)
        sum+=1
        money -= i
print(sum)