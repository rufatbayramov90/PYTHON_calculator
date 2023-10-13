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
calculation_function = operations[symbol_Operations]
answer_first = calculation_function(number1,number2)

print(f"{number1} {symbol_Operations} {number2} = {answer_first}")


symbol_Operations = input("Pick another operation: ")
number3 = int(input("What is the next number? : "))
calculation_function = operations[symbol_Operations]
answer_second = calculation_function(calculation_function(number1,number2),number3)
print(f"{answer_first} {symbol_Operations} {number3} = {answer_second}")
