
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

def main():
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

   
    result = None
    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    else:
        print("Invalid operation.")
        return 1

    # Display the result of the calculation to the console
    if result is not None:
        print("The result is:", result)

if __name__ == "__main__":
    main()
