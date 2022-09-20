
with open("24(1)_sample.txt","r") as f: # don't need to write f.close because it is automatically open and close the file with statment
    a=f.read()

    with open("24(1)_sample.txt","w") as f:
        a=f.write("dii..")

print(a)
