from prettytable import PrettyTable
# create a new table
my_table = PrettyTable()
my_table.add_column("Pokemon Name",["Zigzagoon","Caterpie"],"l")
my_table.add_column("Type",["Normal","Bug"],"l")
my_table.add_row(["Pikachu","Electric"])
print(my_table.align)
print(my_table)
my_table.align='c'
print(my_table.align)
print(my_table)



