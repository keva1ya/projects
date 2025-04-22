x = int(input("Enter a number: "))
y = 0
while x > 0:
    y =y+ x % 10
    x=x// 10
print("The sum of digits is", y)
