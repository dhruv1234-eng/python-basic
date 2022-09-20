myDict = {
    "a": "dhruv",
    "b": "suthar",
    "marks" : [1,2,3,4],
    "anotherdict":{"c":"meena"}

    }
print(myDict['a'])
print(myDict['marks'])
print("\n",myDict)

#we can also create another dict in same dictionary

print("\n",myDict['anotherdict']['c'])

#we can also change the the value in dictionary
myDict['marks']=[56,48]
print(myDict['marks'])
