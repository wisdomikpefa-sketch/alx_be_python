# Simple calculator program

# Take inputs from the user
num1 = float("10")
num2 = float("5")
operation = input("Choose the operation (*, /, +, -): ")

# Perform the operation
if operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero."
elif operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
else:
    result = "Invalid operation."

# Print the result
print("Result:", result)
