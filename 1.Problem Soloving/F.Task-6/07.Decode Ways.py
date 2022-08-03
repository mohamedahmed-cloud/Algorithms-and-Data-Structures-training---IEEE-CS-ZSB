import math
import sys
def solve(s):
    n = len(s)
    my_dict = {n: 1}
    for i in range(n-1, -1, -1):
        if s[i] == "0":
            my_dict[i] = 0
        else:
            my_dict[i] = my_dict[i+1]
        if i+1<n and ( s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
            my_dict[i] +=my_dict[i+2]
    return my_dict[0]

s = sys.stdin.readline()
s = s[:-1]
print(solve(s))


# Wrong answer in tesst 195/269
# def solve(s):
# ans=0
# if s[0]=="0":
#     return ans
# elif int(s)%10==0 :
#     if int(s)<=20:
#         return 1
#     else:
#         return 0

# else:
#     ans+=1
#     for i in range(1,len(s)):
#         if int(s[i-1:i+1])<=26 :
#             if i+1<len(s):
#                 if s[i+1]!="0":
#                     ans+=1
#             else:
#                 ans+=1
#     return ans
