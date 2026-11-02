

def calculator():
    print("\n--- BASIC CALCULATOR ---")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            if b == 0:
                print("Error: Division by zero is not allowed")
            else:
                print("Result:", a / b)
        else:
            print("Invalid operator")

    except ValueError:
        print("Please enter valid numbers")


def currency_converter():
    print("\n--- CURRENCY CONVERTER ---")
    print("1. INR to USD")
    print("2. USD to INR")
    print("3. INR to EUR")
    print("4. EUR to INR")

    try:
        choice = input("Enter choice: ")
        amount = float(input("Enter amount: "))

        if choice == "1":
            print("Result:", amount / 83, "USD")
        elif choice == "2":
            print("Result:", amount * 83, "INR")
        elif choice == "3":
            print("Result:", amount / 90, "EUR")
        elif choice == "4":
            print("Result:", amount * 90, "INR")
        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid amount")


def unit_converter():
    print("\n--- UNIT CONVERTER ---")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Kilogram to Gram")
    print("4. Gram to Kilogram")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")

    try:
        choice = input("Enter choice: ")
        value = float(input("Enter value: "))

        if choice == "1":
            print("Result:", value / 1000, "km")
        elif choice == "2":
            print("Result:", value * 1000, "m")
        elif choice == "3":
            print("Result:", value * 1000, "g")
        elif choice == "4":
            print("Result:", value / 1000, "kg")
        elif choice == "5":
            print("Result:", (value * 9 / 5) + 32, "F")
        elif choice == "6":
            print("Result:", (value - 32) * 5 / 9, "C")
        else:
            print("Invalid choice")

    except ValueError:
        print("Enter a valid number")


def main():
    while True:
        print("\n================================")
        print(" INTERACTIVE CALCULATOR")
        print("       AND UNIT CONVERTER")
        print("================================")
        print("1. Basic Calculator")
        print("2. Currency Converter")
        print("3. Unit Converter")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            unit_converter()
        elif choice == "4":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
