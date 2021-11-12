# greeting
print("Welcome to the tip calculator!")
# ask for input
input_bill = input("What was the total bill? $")
input_tips = input("How much tip would you like to give? 10, 12, or 15?")
input_people = input("How many people to split the bill?")
# covert into float or int
total_bill= float(input_bill)
tips = int(input_tips)
num_people = int(input_people)
# calculate
per_bill = round((total_bill/num_people)*(1+tips/100),2)
bill = (total_bill/num_people)*(1+tips/100)
# display
print(f"Each person should pay: ${per_bill}")
print("Each person should pay: ${0:.2f}".format(bill))
