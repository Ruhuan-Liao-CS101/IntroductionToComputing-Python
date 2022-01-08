# 1) Dictionary tester

info = {"Name": "Sarah",
        "DOB": "09/20/2003",
        "Country": "USA"}

# print all the keys and values
print(info)

# get and print a value based on it's key
print("\nThe information corresponds to name is", info.get("Name"))

# check if a key is in the dictionary ( print true/false)
if 'Country' in info:
    print("\nTrue")
else:
    print("\nFalse")

# clear all values of one dictionary
info.clear()
print("\n", info)

# 2) Word Frequency counter
# create a a string with multiple words ( some duplicated ). 
my_string = 'apple mango orange mango mango orange watermelon strawberry lemon lemon blueberry mango pineapple strawberry strawberry mango apple watermelon apple'

# split all the word of the string. 
my_string = my_string.split()

wordCount = {}

# if word not in the wordCound, give it a value of 1. if word already present +1.
for word in my_string:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1
print("\n", wordCount)



