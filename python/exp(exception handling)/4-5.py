#write a python program to use  finally and else exception handling
def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ValueError:
        print("enter numeric values")
    except ZeroDivisionError:
        print("enter valid number to be divided by (not zero)")
    else:
        print(f"numbers fit for division, the result is {result}")
    finally:
        print("division complete")
divide_numbers()
