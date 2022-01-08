# 5! = 5+4+3+2+1 (= 120)

# create a function that given a number in input returns its factorial. Use a loop solve this.
def factorial_sequential( number ):
    total = 1
    for n in range ( 1, number+1 ):
        total = total + n
    return total

num = 5
print( "The factorial of ", num, "is ", factorial_sequential( num ), "using the sequential method" )

# 5! = 5 + 4 + 3 + 2 + 1
# 5! = 5 + (5-1) + (5-2) + (5-3) + (5-4)
# n! = n + (n-1) + (n-2) + (n-3) + (n-4) ... until 1 (1 is our case)

def factorial_recursive( number ):
    if number == 1:
        return number
    else:
        return number + factorial_recursive(number -1)

print( "The factorial of ", num, "is ", factorial_recursive( num ), "using the recursive method" )

# Exercise 1: calculate the power of number ( .g. 2^4= 2*2^3 =16 ) using both a sequential and a recursive approach

def factorial_sequential( number ):
    total = 2
    for n in range ( 2, number+1 ):
        total = total * n
    return total

num = 2
print( "The factorial of ", num, "is ", factorial_sequential( num ), "using the sequential method" )

def power_recursive( 2, 5 ):
    if power == 1:
        return number
    else:
        return number * power_recursive( number, power-1 )

# Exercise 2: given a list of integer find the max value. Use both the sequential and the recursive approach

def power_recursive( number, power ):
    if power == 1:
        return number
    else:
        return number * power_recursive( number, power-1 )

# Exercise 2: given a list of integer find the sum of all the element. Use both the sequential and the recursive approach