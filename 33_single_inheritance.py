class A:
    Company="youtube"

    def function(self):
        print("dhruv")

class B(A):
    language="py"
    Company="google"
    
    def get(self):
        print("sadanand")

    def function(self):
        print("suthar")

a=A()
a.function()

b=B()
b.function()
print(b.Company)






