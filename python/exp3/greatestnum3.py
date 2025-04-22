x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
z=int(input("Enter the 3rd number: "))
if x>y:
    if x>z:
        print(x, " Is the Greeatest!")
    elif z>x:
        print(z," is greatest of all!")
elif y>x:
    if y>z:
        print(y ," is the greatest!")
    elif z>y:
        print(z," is the greatest")
