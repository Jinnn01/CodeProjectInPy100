import pandas
import pandas as pd

file_path = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

# open csv file with pandas
squirrel_data = pd.read_csv(file_path)
# get fur column
squirrel_fur_color = squirrel_data["Primary Fur Color"]
# get grey squirrel row
grey_squirrel = squirrel_data[squirrel_fur_color == "Gray"]
red_squirrel = squirrel_data[squirrel_fur_color == "Cinnamon"]
black_squirrel = squirrel_data[squirrel_fur_color == "Black"]

# use len get the num of grey squirrel
grey_num = len(grey_squirrel)
red_num = len(red_squirrel)
black_num = len(black_squirrel)
print(grey_num, red_num, black_num)

# construct a data frame
data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_num, red_num, black_num]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_color_sol.csv")
