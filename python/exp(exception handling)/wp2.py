def integer():
    while True:
        try:
            return int(input("enter an integer: "))
        except ValueError:
            print("integer only!!!")
def main():
    num=integer()
    print("NICE, YOU FINALLY ENTERED AN INTEGER!!!!!")
main()