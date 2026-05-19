# SCalculator
def calculator():
    print("=== Simple Calculator ===")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print()
    try:
        # use inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter operation choice (1/2/3/4): ")
        # Perform calculation
        if operation == '1':
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"\n{num1} * {num2} = {result}")
        elif operation == '4':
            # Check for division by zero
            if num2 != 0:
                result = num1 / num2
                print(f"\n{num1} / {num2} = {result}")
            else:
                print("\nError: Cannot divide by zero!")
        else:
            print("\nInvalid operation choice! Please choose 1, 2, 3, or 4.")
    except ValueError:
        print("\nError: Please enter valid numbers!")

if __name__ == "__main__":
    calculator()