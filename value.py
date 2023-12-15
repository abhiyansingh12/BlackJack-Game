# code to identify the value of each card.
pick_a_card = int(input(""))
if pick_a_card >= 2 and pick_a_card <= 10:
    i = pick_a_card
    print("Your hand value is " + str(i) + ".")
elif pick_a_card == 1:
    print("Your hand value is 11.")
elif pick_a_card >= 11 and pick_a_card <= 13:
    print("Your hand value is 10.")
else:
    print("BAD CARD")