a=float(input("enter the value of a: "))
b=float(input("enter the value of b: "))
c=float(input("enter the value of c: "))
d=((b**2)-(4*a*c))
if(d>0):
    print("real and distinct roots")
elif(d<0):
    print("imaginary roots")
else:
    print("the roots are real and same")
r1=((-b)+(d**0.5))/2*a
r2=((-b)-(d**0.5))/2*a
print("the roots are",r1,r2)
