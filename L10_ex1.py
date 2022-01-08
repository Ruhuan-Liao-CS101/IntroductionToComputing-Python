#bad code
a1 = 10
b1 = 15

print("*************************************************************************")
print("The value of a1 is ", a1)
print("The value of b1 is ", b1)
print("The value of a1 + b1 is ", a1+b1)

print("*************************************************************************")
a1 = 12
print("The value of a1 is ", a1)
print("The value of b1 is ", b1)
print("The value of a1 + b1 is ", a1+b1)

print("*************************************************************************")
a1 = 17
print("The value of a1 is ", a1)
print("The value of b1 is ", b1)
print("The value of a1 + b1 is ", a1+b1)

#better code
a1 = 10
b1 = 15
def print_separator():          #if I want to change the separator, I can just adjust it here once instead of 3 times
    print("*************************************************************************")

def add_print_values(val1, va12):               #avoid repeating print functions 
    print("The value of val1 is ", a1)
    print("The value of val2 is ", b1)
    print("The value of val1 + val2 is ", a1+b1)

print_separator()               #no returns for these functions, so must specify where you want it to be used
add_print_values(a1, b1)

print_separator()
a1 = 12
add_print_values(a1, b1)

print_separator()
a1 = 17
add_print_values(a1, b1)

#with return
a1 = 10
b1 = 15
def print_separator():        
    print("*************************************************************************")

def add_print_values(val1, va12):             
    print("The value of val1 is ", val1)
    print("The value of val2 is ", val2)
    print("The value of val1 + val2 is ", val1+val2)

def add_values(val1, val2):
    return val1 + val2

print_separator()          
add_print_values(a1, b1)
print_separator()
print_separator()
print("The value of a1 is ", a1)
print("The value of b1 is ", b1)
print("The value of a1 + b1 is ", add_values(a1+b1))

a1 = 12
add_print_values(a1, b1)

print_separator()
a1 = 17
add_print_values(a1, b1)