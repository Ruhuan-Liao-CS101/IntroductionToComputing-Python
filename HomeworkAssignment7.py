# Halloween candies
# 1) get inputs from user
# 2) save the input of candy to  the list
# 3) print each element in the list with the count (i.e. "Your list has 5 elements including:"m&m, twix...")
# 4) ask user which candy to remove a candy from the list and print the updated list
# 5) ask user to add a new candy to the list and print the updated list
# 6) sort the list and print the sorted list
# 7) print the reverse sorted list


candyList=[]
i = 0
while i <= 4:
    i+=1
    candy=input("Enter a candy please: ")
    candyList.append(candy)
    if i =='5':
        break
    length = len(candyList)
print("Your list has ",length," elements including: ",candyList)

candy = (input("Enter a candy that you want to remove please: "))
candyList.remove(candy)
print(candyList)

candy = (input("Enter a new candy that you want to add please: "))
candyList.append(candy)
print(candyList)

candyList.sort()
print("Sorted list: ", candyList)

candyList.reverse()
print("Reversed list: ", candyList)



# For fun

# One of your neighbors is a dentist who gives to each trick or treater 3 non-sugary treats such as:
# Pencil, apple, toothbrush, eraser, stickers…
# Get this multi-element treat from the user (in a comma separated input request ) 
# and store it in your above list as a sublist (-ie this element in your list is itself a list )
# Print your full list ( including sublist )

# nSugary = ["Pencil", "apple", "toothbrush", "eraser", "stickers", subList]
# print(nSugary)
# user = (input("Enter comma separated multi-element: "))
# subList = user.split (",")
# print(nSugary)


# sublist = []
# for i in subList:
#	subList.append()

# print(subList)