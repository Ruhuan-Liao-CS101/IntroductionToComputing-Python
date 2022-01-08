#semantical or logical error
n1 = 3
n2 = 4
#trying to take the average of 3 and 4, but get 5 as the output
average = n1+n2/2
print(average)
#correction to error
correctAverage = (n1+n2)/2
print(correctAverage)

#runtime error
t = int(input())        #without int, input will be interpreted as a string ... cannot be used for the range
for i in range(t):
    print(i)            #prints all values starting from 0 to the value of t

#exception
actor = {"name": "John Cleese", "rank": "awesome"}
def get_last_name():
    try:
        return actor["last_name"]
    except:
        return "Not there"
print("The actor's last name is ", get_last_name())

#accessing other file
try:
    f = open("my_file.txt", "w")
    try:
        f.write("Writing some data to the file")
    finally:       
        f.close()
except IOError:   
   print("Error: my_file.txt does not exist or it can't be opened for output.")