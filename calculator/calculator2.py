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


def calculator():
    num1 = float(input("What is the first number?: "))
    go = True
    while go:
        for operation in operations:
            print(operation)
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        if input("Do you want to continue or quit? 'c' to continue. 'q' to quit.") == 'c':
            if input("Do you want to continue with the previous value? 'y' to continue. 'n' to start with a new set of numbers.") == 'y':
                num1 = result
            else:
                go = False
                calculator()
        else:
            go = False

calculator()
