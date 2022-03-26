n, p = list(map(int, input().split()))
n1 = 1
n2 = 2
if p == 0:
    print(0, end=' ')
if p == 1 or p == 2:
    print(1, end=' ')
if p == 3:
    print(2, end=' ')
for i in range(4, n+1):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    if(i == p):
        print(n3, end=' ')
        break
