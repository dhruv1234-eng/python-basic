myDict = {
    "a": "dhruv",
    "b": "suthar",
    "marks" : [1,2,3,4],
    "anotherdict":{"c":"meena"}

    }

#print the key into dictonary
print(list(myDict.keys()))


#print the value of the dictonary
print(myDict.values())


#using items print the (key and value) in terms of items
print(myDict.items())


#upadte dict
print(myDict)
upadtemydcit={
    "d":"sadanad"
}
myDict.update(upadtemydcit)
print(myDict)


#get method
print(myDict.get('a'))
print(myDict["a"])

#imp que
print(myDict.get('a2'))#returns none value as it is not present in dictonary
print(myDict["a2"])# its thows an error because this key is not present in dictonary
