class A:
    company="google"

    def function(self):
        print(f"dhurv works in {self.company} and his salary is {self.salary}")

#static method
    @staticmethod
    def fun():
        print("sadanand")

b=A()
b.salary=2000
b.function()
b.fun()
