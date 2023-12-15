# code to print out the game outcome given a hand value.
current_hand_value = int(input(""))
if current_hand_value >= 4 and current_hand_value <= 31:
    if current_hand_value == 21:
        print("BLACKJACK!")
    elif current_hand_value > 21: 
        print("BUST.")
else:
    print("BAD HAND VALUE!")