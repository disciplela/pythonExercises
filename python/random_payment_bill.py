import random

print(f'Who pays the bill for tonight\'s dinner')

string_of_names = input(f'Enter each person\'s name separated by a comma: ')

names = string_of_names.split(',')


print(f'' + names[int(random.random() * len(names))] + ' is going to pay')


#Optional method with randint method
num_items = len(names)
print(random.randint(0, num_items-1))
print(int(random.random() * len(names)))