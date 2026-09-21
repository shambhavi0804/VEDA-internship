def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot find modulus with zero."
    return a % b


def calculator():
    print("=" * 45)
    print("             SIMPLE CALCULATOR")
    print("=" * 45)

    while True:
        print("\nChoose an operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Modulus        (%)")
        print("  6. Exit")
        print("-" * 45)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\nThank you for using the calculator!")
            print("=" * 45)
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please select 1 to 6.")
            continue

        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == "4":
            result = divide(num1, num2)
            symbol = "/"
        else:
            result = modulus(num1, num2)
            symbol = "%"

        if isinstance(result, str):
            print(f"\n{result}")
        else:
            print("\n" + "-" * 45)
            print(f"Result: {num1:g} {symbol} {num2:g} = {result:g}")
            print("-" * 45)


if __name__ == "__main__":
    calculator()