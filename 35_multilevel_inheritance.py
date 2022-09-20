class A:
    name="dhruv"
    surenam="suthar"

    def get(self):
        print("hello")

class B(A):
    fname="sadanad"

    def get(self):
        print("GM")

class C(B):
    city="bardoli"

    def get(self):

        super().get() #note: access super class method 1st then after dervied class run
        print(f"i am living in {self.city}")
a=A()
a.get()
b=B()
b.get()
c=C()
c.get() 



