class A:
    name=100
    surename="suthar"


#using this method we can change the clas attribute
    @classmethod
    def changename(cls,ab):
        cls.name=ab


a=A()
print(a.name)
a.changename("vikey")
print(a.name)



