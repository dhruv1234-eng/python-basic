i=0
while i<10:
    print("yes" + str(i))
    i=i+1
    

#for loop

for i in range(9):
    print(i)


for i in range(3,9):
    print(i)
    

for i in range(1,9,2):
    print(i)
    

#break stament 

for i in range(9):
    print(i)
    
    if i==5:
        break
else:
    print("true")


#continue stament

for i in range(9):
    
    if i==5:
        continue
    print(i)
else:
    print("true")


#pass stament
i = 4

if i>0:
    pass

print("true")
