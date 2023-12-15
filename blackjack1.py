from blackjack_helper1 import *

user_hand = draw_starting_hand("YOUR")
while user_hand < 21:
    output = 'You have ' + str(user_hand) + '.'
    cross_check = input(output + " Hit (y/n)? ") 
    if cross_check.lower() == "y":
        card_value = draw_card()
        user_hand = user_hand + card_value
    elif cross_check.lower() == "n":
        break
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_hand)

dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
    card_value = draw_card()
    dealer_hand = dealer_hand + card_value
print_end_turn_status(dealer_hand)

print_end_game_status(user_hand, dealer_hand)