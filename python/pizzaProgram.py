print(f'Welcome to Python Pizza')

pizzaSize = input(f'What size pizza would you like? ')
add_pepperoni = input(f'Would you like to add pepperoni? ')
extra_cheese = input(f'Would you like to add cheese? ')

bill = 0
if (pizzaSize == 'S'):
    bill+=15
elif(pizzaSize == 'M'):
    bill+=20
else:
    bill+=25

if add_pepperoni == 'Y':
    if pizzaSize == 'S':
        bill+=2
    else:
        bill+=3
if extra_cheese == 'Y':
    bill+=1
else:
    bill+=0
   


print(f'Your final bill is: ${bill}')