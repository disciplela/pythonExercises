row1 = ['☢️', '☢️', '☢️']
row2 = ['☢️', '☢️', '☢️']
row3 = ['☢️', '☢️', '☢️']

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')


position = input("Where do you want to put the treasure? ")
numbers = position.split(' ')

horizontal = int(numbers[0]) 
vertical = int(numbers[1]) 


if horizontal == 1:
    row1[vertical-1] = 'X'

if horizontal == 2:
    row2[vertical-1] = 'X'

if horizontal == 3:
    row3[vertical-1] = 'X'


print(f'{row1}\n{row2}\n{row3}')
