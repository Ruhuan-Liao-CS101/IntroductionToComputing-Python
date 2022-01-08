# exercise 1: Declare 2 variable and assign an integer to each of them. Divide the first number by the second and print the result. Multiply the first number by the second one and print the result. Do not use more than 3 variables.

var1 = 2
var2 = 10
print(var2/var1)
print(var2*var1)

# exercise 2: Given the string "I love Python!" print the first, forth, and the 10th characters.

s = "I love Python!"
print(s[0]+s[3]+s[9])

# exercise 3: Given the quote: "In the end, it's not the years in your life that count. It's the life in your years." A. Lincoln use the slicing operator to print "life in years count". (hint: you might need to use the operator more than once...)

s = '''"In the end, it's not the years in your life that count. It's the life in your years." A. Lincoln'''
print(s[40:44]+s[31:34]+s[25:30]+s[49:55])

# exercise 4: Ask the user to enter their name and store it into a variable. Ask the user to enter their age and store it into another variable. Print the following messages, where the blanks are filled with the correct value:
''' 
"Hi ____ you are _____ years old".
The previous string is long _____
'''

print("What's your name?")
name = input()
print("How old are you?")
age = input()
s1 = "Hi "
s2 = " you are "
s3 = " years old"
print(s1 + name + s2 + age + s3)
s4 = "The previous string is long"
print(len(s4+s1+age+s2+age+s3))






