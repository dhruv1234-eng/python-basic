#use open function to read the contain of the file 
f=open("24(1)_sample.txt","r")
data=f.read()

data=f.read(5)  #read the first 5 character from the file
print(data)
f.close()




