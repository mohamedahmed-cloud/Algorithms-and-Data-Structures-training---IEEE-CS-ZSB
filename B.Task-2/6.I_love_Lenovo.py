# input Operation
number_of_contest=int(input())
contest_score=list(map(int,input().split()))

# Output Operation

# This Make run time error
# amazing_up=0
# amazing_down=0
# if contest_score[1] >contest_score[0]:
#     amazing_down=contest_score[0]
#     amazing_up=contest_score[1]
# else:
#     amazing_down=contest_score[1]
#     amazing_up=contest_score[0]

amazing_up=contest_score[0]
amazing_down=contest_score[0]
counter=0
for i in contest_score:
    if i > amazing_up:
        counter+=1
        amazing_up=i
    if i < amazing_down:
        counter+=1
        amazing_down=i
print(counter)