a=89#global variable
def get():
    global a #fetch a global value
    print(a)

    #change the global value
    a=88#local variable
    print(a)
    
get()
print(a)    
