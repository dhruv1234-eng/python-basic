import random
from re import S

def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return True
        elif you=='si':
            return False
    elif comp=='p':
        if you=='s':
            return True
        elif you=='si':
            return False
    elif comp=='si':
        if you=='s':
            return True
        elif you=='p':
            return False
    
print("comp turn:stone(s) paper(p) or scissor(si)?")
a=random.randint(1,3)
if a==1:
    comp="s"
elif a==2:
    comp="p"
elif a=="3":
    comp="si"

you=input("your turn:stone(s) paper(p) or scissor(si)?")
b=game(comp,you)

if b==0:
     print("tie")
elif b:
    print("win")
else:
    print("lose")

    





    


