class student:
    def __init__(self, name, sapid, marks):
        self.name = name
        self.sapid = sapid
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Sap ID:", self.sapid)
        for sub, mark in self.marks.items():
            print(f"{sub}: {mark}")
students = []
for i in range(4):
    print("enter details->")
    name = input("Enter name:")
    sapid = input("Enter sapid:")
    p = int(input("Enter physics marks:"))
    c = int(input("Enter chemistry marks:"))
    m = int(input("Enter maths marks:"))
    marks = {"physics": p, "chenmistry": c, "math": m}
    s = student(name, sapid, marks)
    students.append(s)
for student in students:
    print("details of student->")
    student.display()
