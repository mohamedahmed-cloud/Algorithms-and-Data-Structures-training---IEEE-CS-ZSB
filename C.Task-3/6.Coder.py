# input Operation
n = int(input())

# output operation
# max_number_of coder
if n % 2 == 0:
    max = (n**2)/2
else:
    max = (n**2)/2+1
# To print arr table from "C","."
big_list = []
sub_list = []
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            sub_list.append("C")
        else:
            sub_list.append(".")
    # print(sub_list)
    big_list.append(sub_list)
    sub_list = []  # To reset the sub_list after adding it to big_list


# For printing The Excepted output
print(int(max))
for i in big_list:
    print("".join(i))
