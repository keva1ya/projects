def negnum():
    raise Exception("Negative number not allowed")
def zeronum():
    raise Exception("Zero isn't a natural number")
def valerror():
    raise Exception("That's not a number at all")
def check(num):
    if num < 0:
        negnum()
    elif num == 0:
        zeronum()
    else:
        return "Natural number!!!!!!!!"
def hi():
    try:
        num = input("Enter a natural number: ").strip()
        if not num.lstrip('-').isdigit():
            valerror()
        num = int(num)
        print(check(num))
    except Exception as e:
        print(f"{e}")
hi()
