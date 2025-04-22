class uni:
    def __init__(hello, name, age,course, semester):
        hello.name = name
        hello.age = age
        hello.course= course
        hello.semester= semester
    def id(hello):
        print(f"{hello.name} is {hello.age} yrs old, studying {hello.course} and is in {hello.semester} semester of college")
me=uni("keval", "19", "B.Tech", "2")
me.id()
x=input("enter name of the student:")
y=input("enter age of the student:")
z=input("enter course of the student:")     
a=input("enter semester of the student:")
other=uni(x, y, z, a)
other.id()