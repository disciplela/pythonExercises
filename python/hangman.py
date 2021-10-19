import random
from os import system, name

def clear():
   # Clear screen using click.clear() function
       # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
from hangman_stages import stages, title
print(title)


#word collection
word_collection = ['wombat', 'apple', 'mississippi', 'roxxann', 'mango', 'harlow']

#word chosen at random
chosen_word = random.choice(word_collection)

#debugging 
# print(f'The secret word is: {chosen_word}')

#array for blank spaces at start of game
blank_spaces = []
#array for already chosen guesses
previous_guesses = []

#creating blank spaces for length of word
for _ in chosen_word:
    blank_spaces.append('_')
print(blank_spaces)

#game loops until end_of_game condition is True
end_of_game = False
attempts = 6
guess = []
while not end_of_game and attempts > 0: 
  guess = input(f'Guess a letter: ').lower()
  
  clear()
  
  if guess in blank_spaces:
    print(f"You've already guessed {guess}")
  
  previous_guesses.append(guess)
  
#Check for guessed letter
  for letter in range(0, len(chosen_word)):
    if guess == chosen_word[letter]:
        blank_spaces[letter] = guess

  if guess not in chosen_word:
    attempts-=1
    print(f'You guessed {guess}, that\'s not in the word. You lose a life')
#clear screen after every guess


  print(stages[attempts])
  print(blank_spaces)
  print(f'Guesses so far: {previous_guesses}')   
  print(f'Lives remaining: {attempts}')

  if '_' not in blank_spaces:
    print(f'You win!')
    end_of_game = True
  if attempts == 0:
    print(f'You lose.')
    end_of_game == True