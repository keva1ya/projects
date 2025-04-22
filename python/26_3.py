class ppl:
    name= "keval"
    occupation="student"
    salary= -50000
    def info (self):
        print(f"{self.name} is a {self.occupation} and makes {self.salary} per month")
p1=ppl()
print(p1.name, p1.occupation, p1.salary)    
p1.info()  
