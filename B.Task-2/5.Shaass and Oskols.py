# input Operation 
# Not solved Yet ==> Try tommorow
number_of_wires=int(input())
number_of_bird_on_each_wire=list(map(int,input().split()))
number_of_shots=int(input())
my_Location=[]
for i in range(number_of_shots):
    my_Location.append(list(map(int,input().split())))
print(my_Location)
# Output Operation
for i in range(number_of_shots):
    for j in range(2):
        wire_to_shots=my_Location[i][0]
        # number_of_bird_on_each_wire[i][wire_to_shots]=0
        if wire_to_shots==1 :
            number_of_bird_on_each_wire[1]+=(number_of_bird_on_each_wire[0]-my_Location[i][1])
            number_of_bird_on_each_wire[0]=0
        elif wire_to_shots==(number_of_wires):
            number_of_bird_on_each_wire[-2]+=(my_Location[i][1]-1)
            number_of_bird_on_each_wire[-1]=0
        else:
            number_of_bird_on_each_wire[wire_to_shots]+=(number_of_bird_on_each_wire[wire_to_shots-1]-my_Location[wire_to_shots-1][1])
            number_of_bird_on_each_wire[wire_to_shots-2]+=(my_Location[wire_to_shots-1][1]-1)
            number_of_bird_on_each_wire[wire_to_shots-1]=0

    print(number_of_bird_on_each_wire)
