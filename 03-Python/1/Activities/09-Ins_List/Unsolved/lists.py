myList = ["Alexander won't code tonight", 333, 'Davud', 76.4]
#print(myList)

myList.append("Artie")
#print(myList)

print(myList[1])

myList.remove("Davud")
print(myList)

print(myList.index(333))

thingPopped = myList.pop(0)
print(myList)
print(thingPopped)