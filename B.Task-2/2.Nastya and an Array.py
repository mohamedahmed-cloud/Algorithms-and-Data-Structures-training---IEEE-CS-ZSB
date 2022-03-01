# input operation 
size_of_array =int(input())
elements_of_array =list(map(int,input().split()))
# output operation 
my_set=set(elements_of_array)
my_list=list(my_set)
out=0  #To count 
# To add one for each not equal element
for i in range(0,len(my_list)):
            if my_list[i]!=0:
                out+=1
print(out)
