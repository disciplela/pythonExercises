print(f'Welcome to the Love Calculator')

name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combinedString = name1 + name2


trueTotal = combinedString.count('t') + combinedString.count('r') + combinedString.count('u') + combinedString.count('e')

loveTotal = combinedString.count('l') + combinedString.count('o') + combinedString.count('v') + combinedString.count('e')

love_score = int(str(trueTotal) + str(loveTotal))


print(f'Love score= {love_score}')

if (love_score < 10) or (love_score> 90):
    print(f'You go together like Coke and Mentos')
elif(love_score > 40) or (love_score < 60):
    print(f'You guys are okay.')
else:
    print(f'No result')