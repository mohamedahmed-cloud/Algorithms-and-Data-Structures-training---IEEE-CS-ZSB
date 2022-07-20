def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
    items_greater = []
    items_lower = []
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
import sys
num=int(sys.stdin.readline())
arr=[int(x) for x in sys.stdin.readline().split()]
a=quick_sort(arr)
print(a)

