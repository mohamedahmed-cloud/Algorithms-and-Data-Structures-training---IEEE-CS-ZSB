# Input Operation
string = input()

# Output Operation

# Counting the "|"
# count_before_plus
i = "|"
j = 0
count_before_plus = 0

while i != "+":
    count_before_plus += 1
    j += 1
    i = string[j]

# print(count_before_plus)

# count_before_equal
i = string[count_before_plus+1]
j = count_before_plus+1
count_before_equal = 0
while i != "=":
    count_before_equal += 1
    j += 1
    i = string[j]
# print(count_before_equal)

# Count after plus
len_string = len(string)
count_after_equal = len_string-(count_before_plus+count_before_equal+2)
# print(count_after_equal)

if count_before_plus+count_before_equal+2 == count_after_equal:
    print("|"*(count_before_plus+1)+"+"+"|" *
          count_before_equal + "=" + "|"*(count_after_equal-1))

elif count_before_plus+count_before_equal == count_after_equal+2 and count_before_plus > 1:
    print("|"*(count_before_plus-1)+"+"+"|" *
          count_before_equal + "=" + "|"*(count_after_equal+1))

elif count_before_plus+count_before_equal == count_after_equal+2 and count_before_plus == 1:
    print("|"*(count_before_plus)+"+"+"|" *
          (count_before_equal-1) + "=" + "|"*(count_after_equal+1))

elif count_before_plus+count_before_equal == count_after_equal:
    print(string)
else:
    print("Impossible")

# antoher Solution
# We can use split to recieve value from the user and split it by depending on these signs "=" and using "+"
# then count it and coplete your soltuion
# it Reduce big notion O
