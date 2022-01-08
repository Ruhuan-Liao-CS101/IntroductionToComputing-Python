# exercise 1
x = 10
if x<0:
    print("x,", x, " is negative.")
print("This is always printed")     # only this statment is printed b/c 10 is NOT negative

# exercise 2
x = 10
if x<0:
    print("x,", x, " is negative.")
else:
    print("x,", x, " is positive.")

# exercise 3
x = 10
y = 10
if x<y:
    print("x is less than y")
else:
    if x>y:
        print("x is greater than y")
    else:
        print("x and y must be equal")

# exercise 4
x = 10
y = 11
if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x and y must be equal")