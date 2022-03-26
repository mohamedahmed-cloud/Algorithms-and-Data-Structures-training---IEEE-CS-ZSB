# input Operation
n, p = list(map(int, input().split()))
# Ouptut Operation
max1 = max(n, p)
min1 = min(n, p)
for i in range(max1, n*p+1, max1):
    if i % n == 0 and i % p == 0:
        print(i)
        break
