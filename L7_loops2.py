#TypeError for combining operands that don't match
    #var1 = input()    ---- made into comments to avoid error in terminal
    #res = var1 + 10
    #print(res)

#Fixing the TypeError
var1 = int(input())
res = var1 + 10
print(res)

var1 = input()
res = int(var1) +10
print(res)

var1 = 7
var2 = " days of the week"
print(str(var1) + var2)

#type() function
var1 = 10
print(type(var1))

var1 = "qwerty"
print(type(var1))

var1 = ["i1", 2, "i3"]
print(type(var1))

#continue in a loop
for letter in "I love Python":
    if letter == "h":
        continue
    print("Current letter:", letter)

#break in a loop
for letter in "I love Python":
    if letter == "e":
        break
    print(letter)
print("The loop is over")