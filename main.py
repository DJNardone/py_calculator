from art import logo

#Calculator
    #Add Fn
def add(n1, n2):
    return n1 + n2

    #Subtract Fn
def subtract(n1, n2):
    return n1 - n2

    #Multiply Fn
def multiply(n1, n2):
    return n1 * n2

    #Divide Fn
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's your first number?: "))
    
    for symbol in operations:
        print(symbol)
    
    go_again = True
    while go_again:
        operation_symbol = input("Pick an operation: ")
        
        num2 = float(input("What's your next number?: "))
        
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation. ") == 'y':
            num1 = answer
        else:
            go_again = False
            calculator()
     
calculator()        
       