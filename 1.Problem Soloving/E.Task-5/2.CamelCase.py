# Input Operation
n=input()
# Ouput Operation
out=1
# equal one because the first word doesn't upper case
for i in n:
    if i==i.upper():
        out+=1
print(out)