days=[31,28,31,30,31,30,31,31,30,31,30,31]
d=int(input("Enter day:"))
m=int(input("Enter month:"))
y=int(input("Enter year:"))
if y%4==0:
    days[1]+=1
    if m<12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m+=1
    elif m==12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m=1
            d=1
            y+=1
else:
    if m<12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m+=1
    elif m==12:
        if d<days[m-1]:
            d+=1
        elif d==days[m-1]:
            m=1
            d=1
            y+=1
print("next date is", d,m,y)