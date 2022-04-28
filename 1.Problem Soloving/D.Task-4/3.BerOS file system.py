# Input Operation
string = input().split("/")

# Output operation
my_list = []
for i in string:
    if i != "":
        my_list.append(i)

print("/"+"/".join(my_list))
