import math
n = int(input())
min=n/math.log(n) #Given function  #make a "Ln" Operation 
max= 1.25506*(n/math.log(n))  #Given function 
print("{:.1f} {:.1f}".format(min, max))