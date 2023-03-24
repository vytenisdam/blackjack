import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    #First step. Both player and computer draws 2 cards each.
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
    
    # If both first cards are aces, second ace value equals to 1.
    if first_card == 11 and second_card == 11:
        computer_points += 1
    else:
        computer_points += int(cards[second_card])
        
    first_card1 = cards.index(random.choice(cards))
    second_card1 = cards.index(random.choice(cards))
    hand.append(cards[first_card1])
    hand.append(cards[second_card1])
    player_points += int(cards[first_card1])
    
    # If both first cards are aces, second ace value equals to 1.
    if first_card1 == 11 and second_card1 == 11:
        player_points += 1
    else:
        player_points += int(cards[second_card1])
        
    print(f"{player_name}'s hand: {hand}")
    print(f' Computer has: {computer_hand[0]}, _')
    
    #Asking player if he/she wants to draw another card.
    should_continue = True
    while should_continue:
        draw_card = input('Would you like another card? y/n ').lower()
        if draw_card == 'y' and player_points < 21:
            extra_card = cards.index(random.choice(cards))
            indexed_extra_card = cards[extra_card]
            #If drawn card is Ace and sum of points > 21 than ace value becomes 1.
            if player_points > 10 and indexed_extra_card == 11:
                hand.append(cards[extra_card])
                player_points += 1      
                print(f' Your {hand}')
            # if not ace stays - 11.
            elif player_points <= 10 and indexed_extra_card == 11: 
                hand.append(cards[extra_card])
                player_points += int(hand[-1])       
                print(f' Your hand: {hand}')
            # any other card has its own unchanged value.
            else: 
                hand.append(cards[extra_card])
                player_points += int(hand[-1])       
                print(f' Your hand: {hand}')
                if player_points > 21:
                    should_continue = False
                    print(f' Your hand: {hand}')
                    print('You got bust!') 
                    play_again = input(f"Hey {player_name}, would you like to play again?")
                    cls()
                else: 
                    should_continue = True          
        else:
            should_continue = False
    #Checks if computer has less than 17 points if so draws another card.
    while 17 > computer_points:
        another_card = cards.index(random.choice(cards))
        indexed_another_card = cards[another_card]
        computer_hand.append(cards[another_card])
        if computer_points < 21 and indexed_another_card == 11:
            computer_points += 1
        else:
            computer_points += int(computer_hand[-1])
    #Calculating a winner.
    if computer_points > 21:
        print(f'{player_name} wins! computer bust.')
        print(computer_hand)
        play_again = input(f"Hey {player_name}, would you like to play again?")
        cls()
    elif computer_points > player_points:
        print(f'Sorry {player_name} you lost. Computer wins!')
        print(f' Your hand: {hand}')
        print(f"Computer's hand: {computer_hand}")
        play_again = input(f"Hey {player_name}, would you like to play again?")
        cls()
    else:
        print(f' Your hand: {hand}')
        print(f"Computer's hand: {computer_hand}")
        print(f'{player_name} wins!')        
        play_again = input(f"Hey {player_name}, would you like to play again?")
        cls()
    #Play one more time.            
    if play_again == 'y':
        hand = []
        computer_hand = []
        blackjack()
    else:
        print('See you later!')
#Start of the game.        
play_game = input('Would you like to play a game of blackjack? Type "y" if so.\n').lower()
if play_game == "y":
    player_name = input('Please enter your name: ')
    blackjack()
else: 
    print('Bye!')

