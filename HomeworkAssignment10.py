# Write a Python script that includes the following 2 functions:

# Function 1:
# takes a dictionary (e.g. d) and a key (e.g. k) as parameters
# checks whether or not k is included in d and prints either "the key is in d" or "the key is not in d" accordingly 

def checkKey(param, key):
    if key in param:
        print("The key is in d", end =" ")
    else:
        (print("The key is not in d"))

param = {'k': 'd'} 
key = 'k'
checkKey(param, key)


# Function 2:
# takes a dictionary (e.g. d) and a key (e.g. k) as parameters
# checks whether or not k is included in d and returns a boolean value (i.e. either true or false accordingly) 

if key in param.keys():
    print("\nTrue")
else:
    print("\nFalse")

