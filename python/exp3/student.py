name=input("enter the name:")
roll=input("enter the roll:")
sem=input("enter the semester:")
sap=input("enter sap:")
course=input("enter course:")

PDS=float(input("enter the name:"))
Python=float(input("enter the name:"))
Chemistry=float(input("enter the name:"))
English=float(input("enter the name:"))
Physics=float(input("enter the name:"))
per=((PDS+Python+Chemistry+English+Physics)/500)*100
cgpa=per/10
grade="a"
if cgpa>0 and cgpa<=3.4:
    grade = "f"
if cgpa>3.4 and cgpa<=5:
    grade ="c+"
if cgpa>5 and cgpa<=6:
    grade ="b"
if cgpa>6 and cgpa<=7:
    grade="b+"
if cgpa>7 and cgpa<=8:
    grade="a"
if cgpa>8 and cgpa<=9:
    grade ="a+"
if cgpa>9 and cgpa<=10:
    grade ="o"
print(name)
print(roll,"\t", sap)
print(sem, "\t", course)
print("subject marks:")
print(PDS,"\n",Physics,"\n",Chemistry,"\n",Python,"\n",English,"\n",per,"\n",cgpa,"\n",grade,"\n")
