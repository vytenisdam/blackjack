import random
#cards = [11,11,11,1,1,1,1,1,1,11,11,11]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hand = []
computer_hand = []

#first draw both players 2 cards
first_card = cards.index(random.choice(cards))
second_card = cards.index(random.choice(cards))
hand.append(cards[first_card])
hand.append(cards[second_card])
first_card = cards.index(random.choice(cards))
second_card = cards.index(random.choice(cards))
computer_hand.append(cards[first_card])
computer_hand.append(cards[second_card])
print(hand)
#print(f' computer has {computer_hand}')

#calculating sum of points in computers hand
computer_points = 0
for points in computer_hand:
    computer_points += int(computer_hand[(computer_hand.index(points))])
    
#check if less than 17 points
while 17 > computer_points:
    another_card = cards.index(random.choice(cards))
    computer_hand.append(cards[another_card])
    computer_points += int(computer_hand[-1])
    #ace if sum < 21, 11 = 11, if sum > 21 11 = 1
    while computer_points < 21 and another_card == 11:
        another_card = 11
    else:
        another_card = 1
        
# player points pt1
player_points = 0
for points in hand:
    player_points += int(hand[(hand.index(points))])
print(f'pirmas{player_points}')

#another card player
should_continue = True
while should_continue and player_points < 21:
    draw_card = input('Would you like another card? y/n ').lower()
    if draw_card == 'y':
        extra_card = cards.index(random.choice(cards))
        indexed_extra_card = cards[extra_card]
        if player_points > 10 and indexed_extra_card == 11:
            hand.append(cards[extra_card])
            player_points += 1      
            print(hand)
            print(f'sitas {player_points}')
        elif player_points <= 10 and indexed_extra_card == 11: 
            hand.append(cards[extra_card])
            player_points += int(hand[-1])       
            print(hand)
            print(f'sitas {player_points}')
        elif player_points > 21:
            should_continue = False
            print(f'You have {hand} player bust.')
        else: 
            hand.append(cards[extra_card])
            player_points += int(hand[-1])       
            print(hand)
            print(f'sitas {player_points}')               
    else:
        should_continue = False
        print(hand)
        
        
        
        #for points in hand:
            #player_points += int(hand[(hand.index(points))])
            #print(computer_hand)
            #print(f' Computer has total of {computer_points} points')
            #print(hand)
            #print(f' You have total of {player_points} points')
            #if player_points > 21:
                #print('player bust')
            #elif computer_points > 21:
                #print('computer bust')
            #elif computer_points > player_points:
                #print('computer wins')
            #else:
                #print('player_wins')
            #print(computer_hand)S
    #again = input('another?')
    #if again == 'y':
    #blackjack()
    #else:
