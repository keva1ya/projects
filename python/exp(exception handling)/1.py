#write a python program to handle divide by 0 exception 
def divzero():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        c = a/b
        print(f"result={c}" ) 
    except ZeroDivisionError:
        print("enter valid number to be divided by (not zero)")

divzero()
