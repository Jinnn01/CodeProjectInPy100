# open the csv file and use readlines() to create a list named data that contains the value from the csv
import pandas

file_path = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/weather_data.csv"

# with csv module
import csv

with open(file_path, "r") as weather_data:
    temperatures = []
    data = csv.reader(weather_data)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas as pd

# dataframe
data = pd.read_csv(file_path)
data_dict = data.to_dict()

# series - get column
temp = data["temp"]
# get average temp solution1
temp_list = temp.to_list()
average_temp = sum(temp_list) / len(temp_list)
# aver_temp solution2
aver_temp = temp.mean()

print(data)
print(data_dict)
print("-------")
print(temp_list)
print("average temp:", average_temp)
print(aver_temp)

# max value
max_value = temp.max()
print(max_value)
print()

# get row from data
monday_data = data[data["day"] == "Monday"]
print(monday_data)
print()

# get the weather of the highest temp day
# print the row of data which had the highest temp
highest_row = data[data["temp"] == data["temp"].max()]
print(highest_row)
# get data from a row
print(monday_data.condition)

# convert monday temp to fahrenheit
monday_temp = int(monday_data.temp)
fah_temp = (9 * monday_temp / 5) + 32
print(f"{monday_temp}C -> {fah_temp}F")

# create a dataframe from scratch
data_dict = {
    "students": ["Joe", "Alex", "Karen"],
    "score": [65, 77, 58]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_csvfile.csv")
