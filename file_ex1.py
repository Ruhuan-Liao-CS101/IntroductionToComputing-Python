# opening a text file for writing
outfile = open("CS101/test.txt", "w")  # utfile = open("PythonFiles/test.text", "w") 
# writing into the using the "write" method
outfile.write("Test\n")
# close the file
outfile.close()

# writing into a file using the compound statement "with"
with open( "CS101/test.txt", "w" ) as outfile:      # change w to a
    outfile.write("Test using with\n")

# reading from a txt file with "with"
with open( "CS101/test.txt", "r" ) as infile:
    print( infile.readline() )