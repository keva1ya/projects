#wap to inheric multilevel and multiple inheritance 
class principal:
    def __init__(self,name,id,batch):
        self.name=name
        self.id=id
        self.batch=batch   
        print ("principal")
        print(f"{self.name}|{self.id}|{self.batch}") 
class teacher(principal):
    def __init__(self,name,id,batch):
        super().__init__(name,id,batch)
class student(teacher):
    def hello(self):
        print("hello")
class janitor(teacher,principal):
    def hi(self):
        print("hi")
s1=student("keval",101,49)
j1=janitor("ramesh",102,50)