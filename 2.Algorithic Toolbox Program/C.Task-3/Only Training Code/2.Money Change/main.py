# link " https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true "

n = int(input())
arr = []
arr = list(map(int, input().split()))
# print(arr)
# sorting
sorting = sorted(arr)
sum = 0
sum2 = 10000000000000000000000
for i in range(0, len(sorting)-1):
    sum = abs(sorting[i]-sorting[i+1])
    if sum2 > sum:
        sum2 = sum
print(sum2)
