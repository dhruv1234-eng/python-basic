#sets which is non repeatable 
a={1,2,3,14,1}
print(type(a))
print(a)


#empty sets
a={}#this syntax will create empty dictionary and not an empty sets plz note it 
print(type(a))


#if you want to create empty set then you will use this syntax
b=set()
print(type(b))


#now if you want add some value in empty set this use this function
b.add(4)
b.add(5)
b.add(5)
b.add(5)#adding a same value into the sets which does not repeat in it
print(b)


#note: you cannot add dictionary and lists into the sets because boths are unhashable type .



