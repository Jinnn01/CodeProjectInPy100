#open the csv file and use readlines() to create a list named data that contains the value from the csv
file_path = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/weather_data.csv"

import csv
with open(file_path, "r") as weather_data:
    # data_readlines = weather_data.readlines()
    # data_list = []
    # for data in data_readlines:
    #     data = data.strip()
    #     data_list.append(data)
    temperatures =[]
    data = csv.reader(weather_data)
    for row in data:
        print(row)
        for tem in row:
            if tem.isdigit():
                temperatures.append(tem)
    print(data)
    print(temperatures)


