# input Operation 
number_of_socks=int(input())
bag_socks=list(map(int, input().split()))
# OutPut operation
table_socks=set() # Note that when we use list don't run on test four because source limitation
max_table_socks=0
for S in bag_socks:
    if S not in table_socks:
        # counter-=1
        table_socks.add(S)
        if len(table_socks)>max_table_socks:
            max_table_socks=len(table_socks)
    else:
        table_socks.remove(S)
print(max_table_socks)

