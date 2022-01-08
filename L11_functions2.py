# function ex 1: using an unknown number of keywords/variables as arguments

def list_students( *students ):                   #add an * before the variable to signify there is x amt of variables 
    for student in students:
        print("The name of the student is: " + student)
list_students("Jill", "Garrin", "Mary", "Rod")


#ex2: using a default parameter/argument
def my_favorite_fruits( fruit="apple" ):
    print("I like ", fruit)

my_favorite_fruits("orange")        #when specified value is present, that value will be used for output
my_favorite_fruits()                #when no specified value is present, the default value (in the defn) will be used
