#write a python to handle multiple exception
def multipleexception():
    try:
        n1=int(input("Enter numerator: "))
        n2=int(input("Enter denominator: "))
        r=n1/n2
        print(f"result={r}")
        dict = {"a": 1, "b": 2}
        key=input("Enter a/b: ")
        print ("value of key ",{dict[key]})  
    except ZeroDivisionError:
        print("enter valid denominator (not zero)")
    except ValueError:
        print("enter valid number")
    except KeyError:
        print("key not found")

multipleexception()
