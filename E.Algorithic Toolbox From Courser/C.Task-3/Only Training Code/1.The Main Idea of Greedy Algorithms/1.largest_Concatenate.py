# We need the max number by concation these digit in sets
my_set = (2, 3, 9, 2, 2)
arr = sorted(my_set)
arr.reverse()
# print(arr)
bigest = ""
for i in arr:
    bigest += str(i)
print(int(bigest))
