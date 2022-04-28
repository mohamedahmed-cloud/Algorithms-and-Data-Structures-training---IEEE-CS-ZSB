# Need give me the optimal solution when i create an number from this array
# Dr.Mostafa saad " https://www.youtube.com/watch?v=90HQlLxMsyA  "
my_arr = [10, 25, 1, 5]
# Note The Greedy algorithm might failed in some test when it failed we should use dynamic programming

# sorting array by reverse order
sorting = sorted(my_arr)
sorting.reverse()

number = 24
arr = []
for i in sorting:
    while i <= number:
        number -= i
        arr.append(i)
print(arr)
