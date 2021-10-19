from calculator_header import calculator_header
from os import system

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

print(calculator_header)
def calculator():
    num1 = float(input('What is the first number?: '))
    for symbol in operations: 
        print(symbol)
    should_continue = True

    while should_continue:

        operation_symbol = input('Choose an operation: ')
        num2 = float(input('What is the next number?: '))


        calculation = operations[operation_symbol] 

        answer = calculation(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        continue_program = input(f'Type "y" to continue calculating with {answer}, or type "n" to start a new calculation: ').lower()
        num1 = answer
        if continue_program == 'y':
            should_continue = True
        else:
            should_continue = False
            system('cls')
            print(calculator_header)
            calculator()

calculator()