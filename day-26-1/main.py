nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [num ** 2 for num in nums]
print(squared_nums)

# Filter even nums
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

# Common nums

with open('file1.txt') as file1:
    list1 = file1.read().split('\n')
with open('file2.txt') as file:
    list2 = file.read().split('\n')

new_list = [int(num) for num in list1 if num in list2]
print(new_list)

# Number of letters in each word of a sentence

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

num_of_letters = {word: len(word) for word in sentence.split()}
print(num_of_letters)

# Weather in c to weather in f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    print(index, row)
    # Access row.student or row.score
    print(row.student, row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
