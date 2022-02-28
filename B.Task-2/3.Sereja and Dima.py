# Input Operation 
number_of_cards=int(input())
cards=list(map(int, input().split()))
# Output Operation 
Sereja_points=0
Dima_points=0
num=2
# To loop on all element in the card list
for i in range(len(cards)):
    if num%2==0 :  #all sereja to choose first 
        if cards[-1]>cards[0]:
            Sereja_points+= cards[-1]
            cards.remove(cards[-1])
            num+=1
        else:
                Sereja_points+= cards[0]
                cards.remove(cards[0])
                num+=1

    else: # Let Dima to choose second TO prevent Dima to choose if there is no elemnt in cards list
        if cards[-1]>cards[0]:
            Dima_points+= cards[-1]
            cards.remove(cards[-1])
            num+=1
        else:
                Dima_points+= cards[0]
                cards.remove(cards[0])
                num+=1
            
print(Sereja_points,end=" ")
print(Dima_points,end=" ")