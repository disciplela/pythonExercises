'''In the third file, called dynomite_dicts.py do the following:

Create an empty dictionary called pokedex.
Add the following key, value pairs to the dictionary:
  'Venosaur': ['Grass', 'Poisen']
  'Charizard': ['Fire', 'Flying']
  'Blastoise': ['Water']

 

Remove 'Blastoise' from the dictionary.'''

pokedex = {
    'venosaur': ['Grass', 'Poison'],
    'Charizard': ['Fire', 'Flying'],
    'Blastoise': ['Water']
}
#before deletion of blastoise
print(pokedex)
del pokedex['Blastoise']

#after deletion of blastoise
print(pokedex)