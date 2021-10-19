row1 = ['☢️', '☢️', '☢️']
row2 = ['☢️', '☢️', '☢️']
row3 = ['☢️', '☢️', '☢️']

map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')


position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) 
vertical = int(position[1]) 

map[vertical - 1][horizontal -1] = 'X'


print(f'{row1}\n{row2}\n{row3}')


#Alternative solution
# selected_row = map[vertical -1]
# selected_row[horizontal - 1] = 'X'

#Alternative syntax
# map[vertical - 1][horizontal -1] = 'X'

#Alternative solution
# if horizontal == 1:
#     row1[vertical-1] = 'X'

# if horizontal == 2:
#     row2[vertical-1] = 'X'

# if horizontal == 3:
#     row3[vertical-1] = 'X'