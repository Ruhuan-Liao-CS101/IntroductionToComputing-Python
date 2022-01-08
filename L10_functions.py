#debugging attempt
for letter in "I love Python":
    if letter == "h":
        continue
    print("Current letter:", letter)

# adding function that will double the input 
x = 5
def dbl(x):
    return 2*x
print(dbl(x))

#stacking
x = 15
def demo(x):
    y = x/3
    z = g(y)
    return z + y + x

def g(x):               #doesn't have to be g(y) b/c the variable will assume any value  
    result = 4*x + 2
    return result

print(demo(x))
print(g(5))     #to evaluate the second function w/ an int that hasn't been assignted to variable 