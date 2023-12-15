# randint to generate random cards. 
from random import randint

# generates random number
card1 = randint(1,13) 
card2 = randint(1,13)

# prints name of the first card generated
if card1 == 1:
    print("Drew an Ace")
elif card1 == 11:
    print("Drew a Jack")
elif card1 == 12:
    print("Drew a Queen")
elif card1 == 13:
    print("Drew a King")
elif card1 == 8:
  print("Drew an 8")
else:
    print(f"Drew a {card1}")

# prints name of the second card generated
if card2 == 1:
    print("Drew an Ace")
elif card2 == 11:
    print("Drew a Jack")
elif card2 == 12:
    print("Drew a Queen")
elif card2 == 13:
    print("Drew a King")
elif card2 == 8:
  print("Drew an 8")
else:
    print(f"Drew a {card2}")

# assigns card value for the generated card
if card1 in [11, 12, 13]:
  card_value1 = 10
elif card1 == 1:
  card_value1 = 11
else:
  card_value1 = card1
if card2 in [11, 12, 13]:
  card_value2 = 10
elif card2 == 1:
  card_value2 = 11
else:
  card_value2 = card2 
cards_value = card_value1 + card_value2
#calculates the cards value in total


if cards_value < 17:
  print(f'Dealer has {cards_value}.')

# if card value is less than 17 it keeps generating a new card
# it then adds the card value of the generated card  until it is equal to 17.
while cards_value < 17:
    new_card = randint(1,13)
    if new_card == 1:
      print("Drew an Ace")
      cards_value += 11
    elif new_card == 11:
      print("Drew a Jack")
      cards_value += 10
    elif new_card == 12:
      print("Drew a Queen")
      cards_value += 10
    elif new_card == 13:
      print("Drew a King")
      cards_value += 10
    elif new_card >= 1 and new_card <= 10:
      if new_card == 8:
        print("Drew an 8")
        cards_value += 8
      else:
        print("Drew a " + str(new_card))
        cards_value += new_card
    if cards_value < 17:
      print(f"Dealer has {cards_value}.")

# it prints out as per the instruction given in Blackjack Game
if cards_value >= 17:
  print(f"Final hand: {cards_value}.")
  if cards_value == 21:
    print("BLACKJACK!")
  elif cards_value > 21:
    print("BUST.")


