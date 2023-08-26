    

def pickOperation():
    operations = ["+", "-", "*", "/"]
    print("\n".join(operations))
    operation = input("Pick an operation: ")
    if(operation not in operations):
        print("Operation not supported")
        return pickOperation()
    return operation

def calculate(first, operation, second):
    if(operation == "+"):
        return first + second
    elif(operation == "-"):
        return first - second
    elif(operation == "*"):
        return first * second
    elif(operation == "/"):
        return first / second
    
def calculator(first = None):
    if(first == None):
        first = float(input("What's the first number?: "))
    operation = pickOperation()
    second = float(input("What's the next number?: "))
    result = calculate(first, operation, second)
    print(f"{first} {operation} {second} = {result}")
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if choice == "y":
        calculator(result)
    elif choice == "n":
        calculator()
    else:
        wantToExit = input("Do you want to exit?  'y' or 'n': ").lower() == "y"
        if(wantToExit):
            return
        else:
            calculator()

calculator()