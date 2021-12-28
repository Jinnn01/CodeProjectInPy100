import pandas as pd

file_path = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

# open csv file with pandas
squirrel_data = pd.read_csv(file_path)
# get fur column
squirrel_fur_color = squirrel_data["Primary Fur Color"]
print(squirrel_fur_color)


def color_counter(count_color):
    color_num = 0
    for color in squirrel_fur_color:
        if count_color == color:
            color_num += 1
        else:
            pass
    return color_num


print("Gray", color_counter("Gray"))
print("Cinnamon", color_counter("Cinnamon"))
print("Black", color_counter("Black"))

# creat new data dict
squirrel_data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [color_counter("Gray"), color_counter("Cinnamon"), color_counter("Black")]
}

# create a dataframe
squirrel_dataframe = pd.DataFrame(squirrel_data_dict)
print(squirrel_dataframe)

# write into a csv file
squirrel_dataframe.to_csv("Squirrel_my_count.csv")
