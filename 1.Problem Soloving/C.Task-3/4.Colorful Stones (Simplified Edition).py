# input Operation 
String_s=list(input())
string_t=list(input())

# output operation
counter=1 
for i in string_t:
    if String_s[counter-1]==i:
        counter+=1

print(counter)
