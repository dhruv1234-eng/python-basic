while(True):
    print("press q for exit")
    a=input("enter a number :")

    if a=="q":
        break

    #it try to excute the code ,in case if try block shows an error then its throw to expeption block
    try:
        a=int(a)
        if a>6:
            print("true")

            #handle try block
    except Exception as e:
        print(f"error{e}")

print("thanks")

