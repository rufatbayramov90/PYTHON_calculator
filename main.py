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

number1 = int(input("What is the first number?: "))
number2 = int(input("What is the second number?: "))


for symbol in operations:
    print(symbol)
symbol_Operations = input("Pick an operation from the line above")
