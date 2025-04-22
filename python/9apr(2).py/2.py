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
    def percentage(self):
        total = sum(self.marks.values())
        return total / 3
    def result(self):
        for mark in self.marks.values():
            if mark < 40:
                return "Fail"
        return "Pass"
def classavg(students):
    classpercentavg = sum(s.percentage() for s in students)
    return classpercentavg / len(students)
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print("enter details->")
    name = input("Enter name: ")
    sapid = input("Enter sapid: ")
    p = int(input("Enter physics marks: "))
    c = int(input("Enter chemistry marks: "))
    m = int(input("Enter maths marks: "))
    marks = {"physics": p, "chenmistry": c, "math": m}
    s = student(name, sapid, marks)
    students.append(s)
for s in students:
    print("details of student->")
    s.display()
print("\nPercentages->")
for s in students:
    print(f"{s.name}: {s.percentage():.2f}%")
print("\nResults->")
for s in students:
    print(f"{s.name}: {s.result()}")
print(f"\nClass Average: {classavg(students):.2f}%")
