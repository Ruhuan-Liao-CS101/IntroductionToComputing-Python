
a1 = 10
b1 = 15

# function used to print a separator
def print_separator():
    print("*************************************************************************")

"""

function used to add 2 numbers and print the result

"""
def add_print_values(val1, val2):
    print("The value of val1 is ", val1)
    print("The value of val2 is ", val2)
    print("The value of val1 + val2 is ", val1+val2)

# function used to add 2 numbers and return a result
def add_values( val1, val2 ):
    return val1+val2

# invking a functiona
print_separator()
#invoking a function
add_print_values( a1, b1 )
print_separator()
print_separator()
print("The value of a1 is", a1)
print("The value of b1 is ", b1)
print("The value of a1 + b1 is ", add_values( a1, b1 ) )

print_separator()
a1 = 12
add_print_values( a1, b1 )

print_separator()
a1 = 17
add_print_values( a1, b1 )



