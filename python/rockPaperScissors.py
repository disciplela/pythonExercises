import random
choice = int(input(f'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

random_selection = random.randint(0,2)

rps = ['rock', 'paper', 'scissors']

if choice > 2 :
    print('Invalid entry')
elif choice > random_selection:
    if (choice == 2 and random_selection == 1):
        print(f'Computer chose {rps[random_selection]}. You chose {rps[choice]} You win!')
    elif (choice == 1 and random_selection == 0):
        print(f'Computer chose {rps[random_selection]}. You chose {rps[choice]} You win!')
    else:
        print(f'Computer chose {rps[random_selection]}. You chose {rps[choice]} You lose.')
elif (choice < random_selection):
    if(choice == 1 and random_selection == 2):
        print(f'Computer chose {rps[random_selection]}. You chose {rps[choice]} You lose!')
    elif (choice == 0 and random_selection == 1):
        print(f'Computer chose {rps[random_selection]}. You chose {rps[choice]} You lose.')
    else:
        print(f'Computer chose {rps[random_selection]}. You chose {rps[choice]} You win.')
elif (choice == random_selection):
        print(f'Computer chose {rps[random_selection]}. You chose {rps[choice]} Tie.')
