# import csv
#
# with open(file="weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data["temp"])
# temp_list = data["temp"].to_list()
# print(round(sum(temp_list) / len(temp_list), 2))
# OR
# print(round(data["temp"].mean(), 2))
# print(data["temp"].max())
# print(data.condition.to_list())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# mon_temp = int(monday.temp)
# fahren = mon_temp * (9 / 5) + 32
# print(fahren)

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(squirrel_data)
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv('squirrel_count.csv')
