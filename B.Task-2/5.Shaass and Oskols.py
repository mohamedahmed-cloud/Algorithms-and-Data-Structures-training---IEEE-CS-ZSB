# I can't simplify it more than this 
# This solution is correct but becuase time limitation can't run on test 27 

# input Operation 

number_of_wires=int(input())
number_of_bird_on_each_wire=list(map(int,input().split()))
# print(number_of_bird_on_each_wire)
number_of_shots=int(input())
my_Location=[]
for i in range(number_of_shots):
    my_Location.append(list(map(int,input().split())))

# Output Operation
for i in range(number_of_shots):
    for j in range(1):
        wire_to_shots=my_Location[i][0]
        if wire_to_shots==1 :
            number_of_bird_on_each_wire[1]+=(number_of_bird_on_each_wire[0]-my_Location[i][1])
            number_of_bird_on_each_wire[0]=0
        elif wire_to_shots==(number_of_wires):
            number_of_bird_on_each_wire[-2]+=(my_Location[i][1]-1)
            number_of_bird_on_each_wire[-1]=0
        else:
            number_of_bird_on_each_wire[wire_to_shots]+=(number_of_bird_on_each_wire[wire_to_shots-1]-my_Location[i][1])
            number_of_bird_on_each_wire[wire_to_shots-2]+=(my_Location[i][1]-1)
            number_of_bird_on_each_wire[wire_to_shots-1]=0

for i in number_of_bird_on_each_wire:
    print(i)
