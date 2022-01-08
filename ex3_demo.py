def add(val1, val2):
    return val1+val2


# example of function using an unknown number of keywords/variables as arguments
def list_students( *students ):
    for student in students:
        print("The name of the student is: " + student)

#list_students( "Jill", "Garrin", "Mary", "Rod" )


#example of function using a default parameter/argument
def my_favorite_fruits( fruit="apple" ):
    print("I like ", fruit)

my_favorite_fruits("orange")
my_favorite_fruits()
