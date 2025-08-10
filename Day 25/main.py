# with open("weather_data.csv") as file:
#     csv_data = file.readlines()
#     stripped_data = [data.strip() for data in csv_data]
#     print(stripped_data)
import pandas
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # for row in data:
#     #     print(row)
#     for tem in data:
#         if tem[1] != "temp":
#             temp_data = tem[1]
#             temperatures.append(int(temp_data))
#     print(temperatures)

import pandas as pd
from numpy.ma import average

csv_data = pd.read_csv("weather_data.csv")
# # print(csv_data)
# print(csv_data["temp"])
#
# data_dict = csv_data.to_dict()
# print(data_dict)


temp_list = csv_data["temp"]
# number_of_days = len(temp_list)
# sum_of_temp = sum(temp_list)
# avg_temp = sum_of_temp / number_of_days
# print(round(avg_temp, 2))

# avg_temp2 = average(temp_list)
# print(round(avg_temp2, 2))
#
# mean_temp = temp_list.mean()
# print(round(mean_temp, 2))
#
# max_temp = temp_list.max()
# print(max_temp)
#
# min_temp = temp_list.min()
# print(min_temp)

#temp_condition = temp_list.condition
# print(csv_data[csv_data.day == "Monday"])
# print(csv_data[csv_data.temp == csv_data["temp"].max()])
#
#
# # Create a DatFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [78, 50, 92]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Create a DataFrame from the squirrel data
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("new_squirrel_data.csv")

grey_squirrel_count = data["Primary Fur Color"]