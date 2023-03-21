import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hand = []
computer_hand = []
first_card = cards.index(random.choice(cards))
second_card = cards.index(random.choice(cards))
hand.append(cards[first_card])
hand.append(cards[second_card])
first_card = cards.index(random.choice(cards))
second_card = cards.index(random.choice(cards))
computer_hand.append(cards[first_card])
computer_hand.append(cards[second_card])
print(hand)
#another card

should_continue = True
while should_continue:
    another_card = input('Would you like another card? y/n ')    
    if another_card == 'y':
        card = cards.index(random.choice(cards))
        hand.append(cards[card])
        print(hand)
    else:
        should_continue = False
        print(hand)
        print(computer_hand)