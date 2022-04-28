# Time Exceed
# Input Operation
n = int(input())

# Ouput Operation
j = 1
sum = 0
out = []
while n > 0:
    if n >= j and n not in out:
        out.append(j)
        n -= j
        j += 1
        sum += 1
        # print(n,j,out)
    else:
        out.remove(j-1)
        out.append(n+j-1)
        # print(out)
        break
print(sum)
# for i in out:
#     print(i,end=" ")
print(' '.join([str(i) for i in out]))


# Pass
# python3
n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()
W = n
prizes = []
for i in range(1, n):
    if W>2*i:
        prizes.append(i)
        W -= i
    else:
        prizes.append(W)
        break

print(len(prizes))
print(' '.join([str(i) for i in prizes]))


#     #
