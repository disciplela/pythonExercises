from os import system, name
from auction_title import title

print(f'{title} SIMULATOR')

resume_bidding = True
new_bidder = {}
highest_bid = 0
winner = ''
while resume_bidding:
    name = input(f'Enter your name: \n')
    bid = int(input(f'Enter your bid: \n$'))
    new_bidder[name] = bid
    add_another_bidder = input('Would you like to add another bidder? "yes" or "no": \n').lower()
    
    if add_another_bidder == 'yes':
        resume_bidding = True
        system('cls')
    else:
        resume_bidding = False
        for bidder in new_bidder:
            if new_bidder[bidder] > highest_bid:
                highest_bid = new_bidder[bidder]
                winner = bidder
                system('cls')

print(f'The highest bid is: ${highest_bid} from {winner}')    

