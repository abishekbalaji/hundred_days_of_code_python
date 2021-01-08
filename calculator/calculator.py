def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

go = "n"
result = 0
stop = "c"

while not stop == "q":
    if go == "n":
        num1 = float(input("What is the first number?: "))
    else:
        num1 = result
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = operations[operation](num1, num2)
    print(result)
    stop = input(
        ("Do you want to continue or quit? 'c' to continue. 'q' to quit."))
    if stop == "c":
        go = input(
            "Do you want to continue with the previous value? 'y' to continue. 'n' to start again.")
