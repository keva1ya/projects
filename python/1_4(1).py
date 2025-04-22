class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print ("Cannot divide by Zero!!!")
            return None
    def modulus(self, a, b):
        return a % b
    def exponentiate(self, a, b):
        return a ** b
calculator = Calculator()
while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus (Remainder Function)")
        print("6. Exponentiate")
        print("7. Exit")
        x = int(input("Enter choice (1/2/3/4/5/6/7): "))
        if x == 7:
            print("Exiting calculator. Goodbye!")
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        match x:
            case 1:
                print("Result:", calculator.add(a, b))
            case 2:
                print("Result:", calculator.subtract(a, b))
            case 3:
                print("Result:", calculator.multiply(a, b))
            case 4:
                print("Result:", calculator.divide(a, b))
            case 5:
                print("Result:", calculator.modulus(a, b))
            case 6:
                print("Result:", calculator.exponentiate(a, b))
            case _:
                print("Invalid input. Please try again.")
