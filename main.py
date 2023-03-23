import random
#cards = [11,11,11,1,1,1,1,1,1,11,11,11]
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hand = []
computer_hand = []
#prideti tuzo keitima i 1 jei iskrenta abu tuzai
#first draw both players 2 cards
def blackjack():
    hand = []
    computer_hand = []
    play_again = 'n'
    player_points = 0
    computer_points = 0
    first_card = cards.index(random.choice(cards))
    second_card = cards.index(random.choice(cards))
    computer_hand.append(cards[first_card])
    computer_hand.append(cards[second_card])
    computer_points += int(cards[first_card])
    if first_card == 11 and second_card == 11:
        computer_points += 1
    else:
        computer_points += int(cards[second_card])
    first_card1 = cards.index(random.choice(cards))
    second_card1 = cards.index(random.choice(cards))
    hand.append(cards[first_card1])
    hand.append(cards[second_card1])
    player_points += int(cards[first_card1])
    if first_card1 == 11 and second_card1 == 11:
        player_points += 1
    else:
        player_points += int(cards[second_card1])
    print('pirmas')
    print(hand)
    print(player_points)
    print(f' computer has {computer_hand}')
    print(computer_points)
    
    #check if less than 17 points
    while 17 > computer_points:
        another_card = cards.index(random.choice(cards))
        indexed_another_card = cards[another_card]
        computer_hand.append(cards[another_card])
        if computer_points < 21 and indexed_another_card == 11:
            computer_points += 1
        else:
            computer_points += int(computer_hand[-1])

        #ace if sum < 21, 11 = 11, if sum > 21 11 = 1
        #placing..........................................
        #if computer_points < 21 and indexed_another_card == 11:
            #another_card = 11
        #else:
            #another_card = 1
        #..................................................

    #another card player
    should_continue = True
    while should_continue:
        draw_card = input('Would you like another card? y/n ').lower()
        if draw_card == 'y' and player_points < 21:
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
            else: 
                hand.append(cards[extra_card])
                player_points += int(hand[-1])       
                print(hand)
                print(f'sitas {player_points}')
                if player_points > 21:
                    should_continue = False
                    print(player_points)
                    print(hand)
                    print(computer_points)
                    print(computer_hand)
                    print('player bust') 
                    play_again = input("Would you like to play again?")                 
        else:
            should_continue = False
            if computer_points > 21:
                print(f'player win, computer bust {computer_points}')
                play_again = input("Would you like to play again?")
            elif computer_points > player_points:
                print('computer wins!')
                print(computer_hand)
                print(computer_points)
                play_again = input("Would you like to play again?")
            else:
                print(hand)
                print(player_points)
                print(computer_hand)
                print(computer_points)
                print('player wwins!')        
                play_again = input("Would you like to play again?")
    if play_again == 'y':
        hand = []
        computer_hand = []
        blackjack()
    elif play_again == 'n':
        print('bye')
blackjack()

