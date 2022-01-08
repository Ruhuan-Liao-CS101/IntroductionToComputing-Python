# Given the list myList = [12, 11, 2, 3, 7, 32, 21, 5, 9]
# use a while loop print each element in the list
# use a for loop to print all elements whose value is even

myList = [12, 11, 2, 3, 7, 32, 21, 5, 9]
length = len(myList)
i = 0

while i < length:
    print(myList[i])
    i += 1

for number in myList:
    if number % 2 == 0:
        print(number, end = " ")

