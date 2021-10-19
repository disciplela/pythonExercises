import random

letters = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print('Welcome to the Pypassword Generator')

pw_letters = int(input(f'How many letters would you like in your password?\n'))
pw_numbers = int(input(f'How many numbers would you like in your password?\n'))
pw_symbols = int(input(f'How many symbols would you like in your password?\n'))
total_characters = pw_letters + pw_numbers + pw_symbols
generated_password = ''
scrambled_password = ''
for character in range(0, pw_letters + 1):
    generated_password += (letters[random.randint(0, pw_letters + 1)])
    
for number in range(0, pw_numbers + 1):
     generated_password += (numbers[random.randint(0, pw_numbers + 1)])

for symbol in range(0, pw_symbols + 1):
     generated_password += (symbols[random.randint(0, pw_numbers + 1)])

for count in range(0, total_characters + 1):
    scrambled_password += (generated_password[random.randint(0, total_characters + 1)])

print(scrambled_password)


# random.shuffle and random.choice are alternative methods and much easier to implement.