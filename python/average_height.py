student_heights = input('Enter each person\'s height followed by a space ').split(' ')
for each_height in range(0, len(student_heights)):
    student_heights[each_height] = int(student_heights[each_height])

#alternative solution using while loop
# i = 0
# total = 0
# while i < len(student_heights):
#     total += student_heights[i]
#     i+=1

total_height = 0
for i in student_heights:   
    total += i

sum_of_students = 0
for x in student_heights:
    sum_of_students += 1
    
print(total)
print(student_heights) 
print(f'Average height rounded to the nearest whole number = {round(total_height/sum_of_students)}')
