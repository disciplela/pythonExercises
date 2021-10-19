print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('Welcome to Treasure Island \n Your mission is to find the treasure.')

choice1 = input(f'You encounter a fork in the road. Choose a direction. "Left" is dark and spooky, "Right" is nice and dreamy.\n ').lower()

if (choice1 == 'right'):
    
    choice2 = input(f'You approach a lake. There are violent fish in the water. Do you "Swim" across or "Wait" until they are gone? \n').lower()
    
    if choice2 == 'wait':
        
        choice3 = input(f'Three doors suddenly appear in front of you. Their colors are "Red," "Blue," and "Yellow." Which color do you choose? \n')
   
        if choice3 == 'yellow':
            print(f'You win!')
        else:
            print(f'Eaten by beasts. Game Over.')
    else:
        choice3 = input(f'You are killed by Trout. Game Over. ').lower()
else:
    print(f'Fall into a hole. Game Over.')
    

