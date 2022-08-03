def solve(summation,n,arr):
    count = 0
    value = numpy.zeros((summation+1, n+1))
    # print(value)
    for i in range(1, summation+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if arr[j-1]<=i:
                temp = value[i-arr[j-1]][j-1] + arr[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == summation: count += 1
    if count < 3: print('0')
    else: print('1')

import numpy
n=int(input())
arr=list(map(int,input().split()))
summation=sum(arr)
my_set=len(set(arr))
if n<3:
    print('0')
elif summation%3!=0:
    print('0')
elif my_set==1 and summation%3!=0:
    print('0')
else:
    solve(summation//3,n,arr)