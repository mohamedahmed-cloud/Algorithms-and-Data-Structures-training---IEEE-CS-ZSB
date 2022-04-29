# Input Operation 
my_s=input()
n=int(input())
arrin=[]
for i in range(n):
    arrin.append(int(input()))

# OutPut Operation 
arrout={}
weight=0
for i in range(len(my_s)):
    if i==0 or my_s[i]!=my_s[i-1]:
        weight=ord(my_s[i])-ord('a')+1
    else:
        weight+=ord(my_s[i])-ord('a')+1
    arrout[weight]=1
for i in arrin:
    if i in arrout:
        print("Yes")
    else:
        print("No