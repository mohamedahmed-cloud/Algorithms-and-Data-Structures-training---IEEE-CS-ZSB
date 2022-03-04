# INput operation
lines=int(input())
seats=[]
for i in range(lines):
    seats.append(input().split("|"))

# Output operation
result=""
for i in range(len(seats)):
    for j in range(2):
        if seats[i][j] =="OO" :
            result="Yes"
            seats[i][j] = "++"
            break
        else:
          result="No"
    if result =="Yes" :
        print (result)
        break  
if result=="No":
        print(result)
else:       
    for i in seats:
        print("|".join(i))
       