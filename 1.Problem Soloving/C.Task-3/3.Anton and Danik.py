# Input Operation 
games_played=int(input())
who_own=input()

# Ouput Operation 
Anton=who_own.split('D')

len_of_all=len(who_own)
number=0
for i in range(len(Anton)):
    if "A" in Anton[i]:
        number+=len(Anton[i])

if number>(len_of_all/2):
    result="Anton"
elif number==(len_of_all/2):
    result="Friendship"
else:
    result="Danik"
print(result)