# Python3
n, W = list(map(int, input().split()))
lst = []

if W == 0:
    print(0)
    quit()

for i in range(n):
    v, w = list(map(int, input().split()))
    if v == 0:
        continue
    lst.append((v, w))
print(lst)
lst.sort(key = lambda x: x[0]/x[1], reverse = True)
print(lst)
total_value = 0

for v,w in lst:
    if W==0:
        print(total_value)
        quit()
    amt = min(w, W)
    total_value += amt*v/w
    W -= amt

print(total_value)