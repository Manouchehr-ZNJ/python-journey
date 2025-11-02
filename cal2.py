print("=== Smart Calculator ===")
print("Type 'exit' to quit\n")

while True:
    # Get input
    user_input = input("Enter calculation (e.g., 5 + 3) or 'exit': ")
    
    # Check for exit
    if user_input == "exit":
        print("Goodbye!")
        break
    
    # Split input into parts
    try:
        num1_str, op, num2_str = user_input.split()
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        # Calculate
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result = "Error: Cannot divide by zero!"
            else:
                result = num1 / num2
        else:
            result = "Error: Invalid operator!"
        
        print(f"Result: {result}\n")
        
    except:
        print("Error: Invalid input! Use format: number operator number\n")