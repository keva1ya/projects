class student:
    def display(self):
        print("i am a student")
class teacher(student):
    def display(self):
        print("no ur not")
p = student()
s = teacher()
p.display()
s.display()
