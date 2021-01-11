import random

nums = [1, 2, 3, 4]
new_list = [num + 1 for num in nums]
print(new_list)
name = "Abishek"
new_name_list = [letter for letter in name]
print(new_name_list)

new_range_list = [num * 2 for num in range(1, 5)]
print(new_range_list)

even_list = [num for num in range(1, 11) if num % 2 == 0]
print(even_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 4]
print(short_names, long_names)

# Dictionary Comprehension

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
