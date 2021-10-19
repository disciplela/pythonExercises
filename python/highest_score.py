scores = input('Enter a list of scores separated by a space:\n').split(' ')

for x in range(0, len(scores)):
    scores[x] = int(scores[x])

highest_score =0
for score in scores:
    if score > highest_score:
        highest_score = score
print(f'The highest score is: {highest_score}')