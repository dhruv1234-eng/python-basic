class A():
    salary=5000
    bounssalary=500
    

    @property
    def function(self):
        print(f"total: {self.salary+self.bounssalary}")

    @function.setter
    def function(self,val):
        self.bonussalary=val-self.salary

a=A()
a.function
a.function=6000
print(a.bonussalary)



