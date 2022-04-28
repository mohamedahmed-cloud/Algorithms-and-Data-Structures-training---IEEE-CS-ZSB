# Input Operation
s_small = list(input())
lang = len(s_small)
t_large = input()
# Ouput Operation

# Note That We end loop by "-1" to if there string it's len =1 it can be make a for loop
for i in range(lang-1, -1, -1):

    if s_small[i] == "z":
        s_small[i] = "a"  # assign "a" to s_small[i]
    else:
        s_small[i] = chr(ord(s_small[i])+1)
        break
s_small = "".join(s_small)
# print(s_small)
if s_small >= t_large:
    print("No such string")
else:
    print("".join(s_small))
