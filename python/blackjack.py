'''second attempt'''

from functools import cache
from os import system
import random
from blackjack_logo import logo

def deal_card():
    '''Returns random card from list of cards'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)   

def calculate_score(cards):
    '''Takes list of cards and returns total calculated score from cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare_scores(player_score, dealer_score):
    if player_score == dealer_score:
        return 'Draw'
    elif dealer_score == 0:
        return 'Dealer has Blackjack! Dealer wins.'
    elif player_score == 0:
        return 'Player has Blackjack! Player wins'
    elif player_score > 21:
        return 'Player bust. Dealer wins.'
    elif dealer_score > 21:
        return 'Dealer bust. Player wins.'
    elif player_score > dealer_score:
        return 'Player wins.'
    else:
        return 'You lose.'    


def blackjack():
    print(logo)
        
    player_hand = []
    dealer_hand =[]
    is_game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card()) 

    while not is_game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f'    Your cards: {player_hand}, current score: {player_score}')
        print(f'    Dealer\'s first card: {dealer_hand[0]} dealers hand{dealer_hand}')

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            hit_player = input('Type "y" to hit, or type "n" to stay: ').lower()
            if hit_player == 'y':
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while dealer_score !=0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    print(f'    Player\'s cards: {player_hand} and final score {player_score}')
    print(f'    Dealer\'s hand {dealer_hand} and final score {dealer_score}\n')

    print(compare_scores(player_score, dealer_score))

    play_again = input('Would you like to play again?: "y" or "n" ').lower()

    if play_again == 'y':
        system('cls')
        blackjack()
    else:
        print('Thanks for playing.')        

play_blackjack = input('Would you like to play Blackjack?: "y" or "n" ').lower()

if play_blackjack == 'y':
    system('cls')
    blackjack()
else:
    print('Thanks for playing.')



'''first attempt'''
# from os import system
# import random
# from blackjack_logo import logo

# #function to generate random card from deck
# def random_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     return random.choice(cards)   

# #function to hit and update score 
# def hit(total_hand, total_score, no_of_draw):
#     total_score = 0
#     for _ in range(0, no_of_draw):
#         total_hand.append(random_card())
#     for _ in range(0, len(total_hand)):
#         total_score += total_hand[_]    
#     return total_hand, total_score

# def blackjack():
    
#     print(logo)
    
#     player_hand = []
#     player_score = 0
#     dealer_hand =[]
#     dealer_score = 0

#     player_hits = True
#     dealer_hits = True

#     player_hand, player_score = hit(player_hand, player_score, 2)
#     dealer_hand, dealer_score = hit(dealer_hand, dealer_score, 2)
#     print(f'Your cards: {player_hand}, current score: {player_score}')
#     print(f'Dealer\'s first card: {dealer_hand[0]} dealers hand{dealer_hand}')

# #while loop to detect when user chooses y or n
#     while player_hits == True:
#         if player_score > 21:
#             if 11 in player_hand:
#                     ace = player_hand.index(11)
#                     player_hand[ace] = 1
#                     player_score -= 10
#                     print(f'Your updated cards: {player_hand}, updated score: {player_score}')
#             else:
#                 print('Player bust. Dealer wins.')
#                 player_hits = False
#                 dealer_hits = False
        
#         elif player_score < 21:
#             response = input(f'Would you like to hit? "y" or "n": ').lower()
#             if response == 'y':
#                 player_hand, player_score = hit(player_hand, player_score, 1)
#                 print(f'Your cards: {player_hand}, current score: {player_score}')
#             elif response == 'n':
#                 player_hits = False
#         elif player_score == 21:
#             print('Blackjack. Player wins!')
#             player_hits = False
#             dealer_hits = False
    
#     #while loop to detect if dealer is over 17 and if so quits hitting more cards
#     while dealer_hits:
#         if dealer_score > 21:
#             if 11 in dealer_hand:
#                 convert_to_ace = dealer_hand.index(11)
#                 dealer_hand[convert_to_ace] = 1
#                 dealer_score -= 10
#                 dealer_hits = True
#             else:
#                 if dealer_score == 21:
#                     print('Blackjack! Dealer wins.')
#                 elif dealer_score > 21:
#                     print('Dealer bust. Player wins.')  
#                 elif dealer_score > player_score:
#                     print('Dealer has higher score. Dealer wins.')
#                 elif dealer_score < player_score:
#                     print('Player has higher score. Player wins.')
#                 else: 
#                     print('Draw')
#                 dealer_hits = False
#         if dealer_score <= 16:
#             dealer_hand, dealer_score = hit(dealer_hand, dealer_score, 1)
#             dealer_hits = True

  
# #print final decision and scores
#     print(f'Player\'s final cards: {player_hand}, Player\'s final score: {player_score}')
#     print(f'Dealer\'s final cards: {dealer_hand} Dealer\'s final score: {dealer_score}')
# #prompts user if they would like to play again.                
#     play_again = input('Would you like to play again? "y" or "n": ')
#     if play_again == 'y':
#         system('cls')
#         blackjack()
#     else:
#         print('Goodbye.')
            
# #prompts user if they would like to play blackjack
# play_blackjack = input('Do you want to play a game of Blackjack? Type "y" or "n" for no: ').lower()
# continue_game = True

# if play_blackjack == 'y':
#     system('cls')
#     blackjack()

# else:   
#     print('Goodbye')

