#code to identify the name of each card.
pick_a_card = int(input(""))
if pick_a_card >= 2 and pick_a_card <= 10: 
    if pick_a_card == 8:
        print("Drew an 8")
    else:
        i = pick_a_card
        print("Drew a " + str(i)) 
elif pick_a_card == 11:
    print("Drew a Jack")
elif pick_a_card == 12:
    print("Drew a Queen")
elif pick_a_card == 13:
    print("Drew a King")
elif pick_a_card == 1:
    print("Drew an Ace")
else:
    print("BAD CARD")