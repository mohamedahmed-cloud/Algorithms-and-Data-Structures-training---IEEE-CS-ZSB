#   input Operation
first_line = input().split()
n, m, k = int(first_line[0]), int(
    first_line[1]), int(first_line[2].split('.')[1])
#   OutPut Operation
b = {}
for i in range(n):
    old_skill = input().split()
    c = int(old_skill[1])*k/100
    if c >= 100:
        b[old_skill[0]] = c
for i in range(m):
    d = input()
    if not (d in b):
        b[d] = 0
print(len(b))
for i in sorted(b):
    print(i, int(b[i]))
