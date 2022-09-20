
class A:
    def __init__(self,name,company):

        self.name=name
        self.company=company
    def function(self):
        print(f"employee name is {self.name} ")
        print(f"employee works in {self.company} company")

b=A("dhruv","google")

b.function()

 