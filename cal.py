def calculate(num1, num2, operator):
    """
    Calculate two numbers with given operator
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Error: Invalid operator!"


def main():
    print("=== Smart Calculator ===")
    print("Example: 5 + 3")

    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        op = input("Operator (+ - * /): ").strip()

        result = calculate(num1, num2, op)
        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter numbers only!")


if __name__ == "__main__":
    main()
    