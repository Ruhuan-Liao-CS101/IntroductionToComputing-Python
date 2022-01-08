# generate random number
import random
nr = random.randint(1, 99)
print(nr)

# list
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])

# sublist/nested list
myList = [1, 2, 3, [1, 2, 3]]
print(myList[3])

# combining lists
print([1, 2] + [3, 4])

# in operator 
print("teacher" in ["student", "teacher", "principal"])

# keyword del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# del thislist
# print(thislist) --- will give error

# remove 
thislist = ["apple", "banana", "cherry"] 
thislist.remove("banana")
print(thislist)

# length
length = len(myList)
print("The list myLife has", length, " elements/items")

# printing each element w/ loop and length
i = 0
while(i<len(myList)):
    print(myList[i])
    i = i+1