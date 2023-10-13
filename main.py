def add(n1,n2):
    return n1 +n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide 
}

def calculator():   
    number1 = float(input("What is the first number?: "))

    for symbol in operations:
    print(symbol)
    should_continue = True


    while should_continue:
        symbol_Operations = input("Pick an operation:  ")
        number2 = float(input("What is the second number:  "))
        calculation_function = operations[symbol_Operations]
        answer = calculation_function(number1,number2)

        print(f"{number1} {symbol_Operations} {number2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ")=="y":
            number1 = answer
        else:
            should_continue = False
            calculator()
calculator()



 