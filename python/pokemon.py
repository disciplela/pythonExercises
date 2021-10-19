#tuple name pokemon that holds strings 'pikachu', 'charmander', 'bulbasaur'
pokemon = ('pikachu', 'charmander', 'bulbasaur')

#print index 1 of tuple pokemon
print(pokemon[1])

#unpack the values in the following variables: starter1, starter2, starter3
starter1, starter2, starter3 = pokemon
example = 'this is fun'
#create a tuple using tuple() method that contains letters of your name
name = tuple('sean')

#check whether 'i' is in your representation of your name
count = name.count('i')
print(f'There is this many iternations of the letter \"i\": {count}')
#for loop that prints integers 2 thru 10
for i in range(2,11):
    print(i)

#while loop that prints integers 2 thru 10
x = 2
while x < 11:
    print(x)
    x+=1

#for loop that iterates over string 'this is a simple string' and prints each character

simple_string = 'this is a simple string'
for letter in simple_string:
    print(letter)

#nested loop that iterates over the following set ('this','is','a','simple','set')
string_set = {'this', 'is', 'a', 'simple', 'set'}

for x in string_set:
    # print(x)
    i = 0
    while i < 3:
        print(x)
        i+=1
