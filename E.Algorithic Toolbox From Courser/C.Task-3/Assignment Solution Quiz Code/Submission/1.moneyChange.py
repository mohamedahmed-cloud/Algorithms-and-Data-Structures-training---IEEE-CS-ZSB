money = int(input())
count = 0
for i in [10, 5, 1]:
    if money>=i:
        q = money//i
        count += q
        money = money%i
        if money==0:
            print(count)
            quit()