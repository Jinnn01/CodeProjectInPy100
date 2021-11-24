# Calculator
import art
# add function
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def Multiply(n1, n2):
    return n1 * n2


# Divide
def Divide(n1, n2):
    return n1 / n2


# Create a dict{symbol:function}
operations = {
    "+": add,
    "-": subtract,
    "*": Multiply,
    "/": Divide
}
# above value are functions

def calculator():
    print(art.logo)
    # ask user to input
    num1 = float(input("What's the first number?: "))

    # loop through the dict and print out the symbol
    for symbol in operations:
        print(symbol)

    # ask symbol
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))

    # operation_function is function
    operation_function = operations[operation_symbol]
    # call the function
    answer = operation_function(num1, num2)

    # display
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # continue_flag
    continue_flag = True

    while continue_flag:
        # ask user to continue or not
        con_calculation = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new one, 'exit' to exit.:")

        if con_calculation == "n":
            calculator()
        if con_calculation =="exit":
            break
        # ask for another num and operation
        operation2 = input("Pick anther operation: ")
        num3 = float(input("What's the next number?: "))
        operation_function = operations[operation2]
        past_answer = answer
        answer = operation_function(answer, num3)

        # display
        print(f"{past_answer} {operation2} {num3} = {answer}")
calculator()
