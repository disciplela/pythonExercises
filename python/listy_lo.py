
#Create a list named food with two elements 'rice' and 'beans'.

food = ['rice', 'beans']

#Append the string 'broccoli' to food using .append().

food.append('broccoli')

print(food)

#Add the strings 'bread' and 'pizza' to food using .extend().

additional_items = ('bread','pizza')

food.extend(additional_items)

print(f'The following list is extended: {food}')

#Print the first two items in the food list using print() and slicing notation.

list_slice = food[slice(0,2)]

print(f'First two items in a list {list_slice}')

#Print the last item in food using print() and index notation.

print(f'Last two items in the list {food[-2:]}') 

#Create a list called breakfast from the string "eggs,fruit,orange juice" using the split() method.

breakfast_items = "eggs, fruit, orange juice"

breakfast = breakfast_items.split(',')

print(f'Here is the sliced breakfast_items list: {breakfast}')
#Verify that breakfast has 3 elements using the len built-in.

print(f'There are {len(breakfast)} breakfast items in the list')


#prompts the user for a floating-point value until they enter stop. Store their entries in a list, and then find the average, min, and max of their entries and print them those values.
 
continue_loop = 'y'
floating_number_list = []

while continue_loop == 'y':
    floating_number = float(input('Enter a floating point value: '))
    floating_number_list.append(floating_number)
    continue_loop = input('Would you like to continue? \"y\" for yes or \"n\" for no? ').lower()

print(f'The floating point number list {floating_number_list}\nThe min is {min(floating_number_list)}\n The max is {max(floating_number_list)}\n The average is {round(sum(floating_number_list)/len(floating_number_list),2)}')