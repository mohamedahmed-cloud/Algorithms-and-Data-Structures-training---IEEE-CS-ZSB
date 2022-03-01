# Input Operation 
number_of_problems,solving_skills=list(map(int,input().split()))
problems=[]
problems.append(list(map(int,input().split())))
# Output Operation
counter=0 
j=1
my_Second_counter=0
for i in range(number_of_problems):
    if problems[0][-j]<=solving_skills:
        counter+=1   
        j+=1
        my_Second_counter+=1
    else:
        break
j=0
if my_Second_counter==number_of_problems:
    pass
else:
    for i in range(number_of_problems):
        if problems[0][j]<=solving_skills:
            counter+=1 
            j+=1
        else:
            break
    
print(int(counter))