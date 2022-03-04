# Inpout Operation
char_numbers=int(input())
char=input().split('W')

# Ouput Operation 
len_1=0 
for i in range(len(char)):
    if "B" in char[i]:
        len_1+=1
print(len_1)
for i in range(len(char)):
    if "B" in char[i]:
        print(len(char[i]),end=" ")
