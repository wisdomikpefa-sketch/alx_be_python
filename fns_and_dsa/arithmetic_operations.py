def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    
    if operation == "add":
        result = num1 + num2
        print(f"Result: {result}")

    elif operation == "subtract":
        result = num1 - num2
        print(f"Result: {result}")

    elif operation == "multiply":
        result = num1 * num2
        print(f"Result: {result}")

    elif operation == "divide":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {result}")
