y = 1
j = 100
c = 0

while y <= j:
    if y % 5 == 0 or y % 7 == 0:
        c =c+ 1
        print(y)
    y =y+ 1

print("Total numbers divisible by 5 or 7:", c)
