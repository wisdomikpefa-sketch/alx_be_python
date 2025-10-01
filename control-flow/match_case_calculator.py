# Simple multiplication calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (*, ): ")

if operation == '*':
    result = num1 * num2
    print("Result:", result)
else:
    print("Invalid operation. Only '*' is supported.")
