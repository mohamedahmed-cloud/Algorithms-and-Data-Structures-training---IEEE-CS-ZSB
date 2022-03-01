# input Operation 
number_of_socks=int(input())
bag_socks=list(map(int, input().split()))
# OutPut operation
table_socks=set()
# counter_list=[]
max_table_socks=0
# counter=0

for S in bag_socks:
    if S not in table_socks:
        # counter-=1
        table_socks.add(S)
        if len(table_socks)>max_table_socks:
            max_table_socks=len(table_socks)
        
       
        # counter_list.append(counter)
    else:
        table_socks.remove(S)

        # counter+=1
        # counter_list.append(counter)
print(max_table_socks)

########################################################################
# n= int(input())
# array=list(map(int,input().split()))
# sets=set()
# c=0
# for x in array:
#     if x not in sets:
#         sets.add(x)
#         c=max(len(sets),c)
#     else:
#         sets.remove(x)
# print(c)