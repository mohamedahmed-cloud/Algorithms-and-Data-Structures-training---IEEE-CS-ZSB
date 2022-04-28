# Solution
out = []
arr = [3, 30, 34, 9]
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if int(str(arr[i])+str(arr[j])) < int(str(arr[j])+str(arr[i])):
            swap = arr[i]
            arr[i] = arr[j]
            arr[j] = swap
    print(arr)

    # out.append(i)
# print(" ".join(arr))
out = "".join(str(i) for i in arr)
print(int(out))
