n, m, k = list(map(float, input().split()))
n = int(n)
m = int(m)
k = list(k).split('.')[1]
# print(k)
b = {}
print(k.split(""))
# for i in range(n):
#     old_skills = input().split()
#     c = int(old_skills[1])*k
#     if c >= 100:
#         b[old_skills[0]] = c
# # print(b)
# for _ in range(m):
#     new_skills = input()
#     if not (new_skills in b):
#         b[new_skills] = 0

# print(len(b))
# # print(b)
# for skills in sorted(b):
#     print(skills, int(b[skills]))

# ######################################################################
a = input().split()
n, m, k = int(a[0]), int(a[1]), int(a[2].split('.')[1])
print(k)
# b={}
# for i in range(n):
#     a=input().split()
#     c=int(a[1])*k/100
#     if c>=100: b[a[0]]=c
# for i in range(m):
#     d=input()
#     if not (d in b): b[d]=0
# print(len(b))
# for i in sorted(b):
#     print(i,int(b[i]))
