# input Operation
stone_number=int(input())
stone_color=list(input())

# output Operation 
min_removed=0
for i in range(stone_number-1):
    if stone_color[i]==stone_color[i+1]:
        min_removed+=1
print(min_removed)