# differences between " and '
print('It\'s Python')
print('XV' + 'II')

# examples with the slicing operator
s = 'harvey eats toomuch'
s[3]
print(s[3])

message = "Hello out there!"
print(message[:5])         # "Hello"
print(message[6:9])       # "out"
print(message[10:])       # "there!"
print(message[-5:-1])        # ”!”
print(message[0:10:2]) # "Hloot"

# example using the len() function
print( len(message) )

# example of the input function
print("What is your name ?")
name = input()
print("Hi ", name, "!")
nc = len(name)
print(nc)



