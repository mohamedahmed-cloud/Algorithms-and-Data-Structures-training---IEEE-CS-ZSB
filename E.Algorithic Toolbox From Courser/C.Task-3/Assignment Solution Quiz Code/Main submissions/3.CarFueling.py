import math
d = int(input())
m = int(input())
n = int(input())
arr = list(map(int, input().split()))
out = math.ceil(d/m)-1
check = 1
for i in range(1, len(arr)):
    if abs(arr[i]-arr[i-1]) <= m:
        # print(abs(arr[i]-arr[i-1]))
        check = 1
    else:
        check = 0
        break
    if d-arr[-1] > m:
        check = 0
        break
if check == 1:
    print(out)
else:
    print(-1)
