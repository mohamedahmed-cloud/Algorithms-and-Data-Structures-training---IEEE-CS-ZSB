# This solution by Greedy algorithm might failed with some test case so if it is failed use dynamic programming
money = 30
arr = [5, 1, 10]
sorting = sorted(arr)
sorting.reverse()
out = []
for i in sorting:
    while i <= money:
        out.append(i)
        money -= i
print(out)
