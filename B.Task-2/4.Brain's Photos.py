# input operation
Black_White=["B","W","G"]
Colored=["C","M","Y"]
n,m=list(map(int,input().split()))
# output Operation
my_list=[]
for i in range(n):
    Colors=list(map(str,input().split()))
    my_list.append(Colors)
for i in my_list:
        if "C" in i or "M" in i or "Y" in i :
            output="#Color"
            break
        else:
            output="#Black&White"
print(output)