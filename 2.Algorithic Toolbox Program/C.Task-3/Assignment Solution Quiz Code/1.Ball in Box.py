
# her is a small error needed to develop when you make a check i == 9 you don't make a check if sum_of_needed_numbers-sm is in out array or not :
# this point need to develop 
# we have 10 box fill them with differnt number to reach 60
import random
sum=0
out=[]
sum_of_needed_numbers=60
for i in range(10):
    myvalue=True
    if i==9:
        out.append(sum_of_needed_numbers-sum)
        break
    while myvalue :
        rand=int(random.randint(0,10))
        if rand not in out and sum < sum_of_needed_numbers:
            sum+=rand
            out.append(rand)
            myvalue=False

print(sum)
print(out)
print(len(out))
# check
sum=0
for i in out:
    sum+=i
print(sum)