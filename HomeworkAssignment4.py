x = int(input("Enter the first interger please: "))
y = int(input("Enter the second interger please: "))
z = int(input("Enter the third interger please: "))

if (x<=y and x<=z):
    print(x, "is the smallest")
elif (y<=x and y<=z):
    print(y, "is the smallest")
else:
    print(z, "is the smallest")

