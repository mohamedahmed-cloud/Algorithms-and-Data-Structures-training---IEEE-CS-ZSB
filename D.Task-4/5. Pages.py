# Input Operation
n, p, k = list(map(int, input().split()))

# OutPut Operation
page = []
if p-k > 1:
    page.append("<<")
for i in range(max((p-k), 1), min((p+k), n)+1):
    if i == p:
        page.append("("+str(p)+")")
    else:
        page.append(str(i))

if p+k < n:
    page.append(">>")

print(" ".join(page))
