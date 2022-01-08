# differences between " and '

print("It's Python")

        # print('It's Python') python reads the ' in it's as the end of the string -- needs to use ""
print('XL' + 'II')
print('VI' * 7)

str(42)
len('42')
print(len('42'))

# string index
s = 'harvey eats toomuch'
print(s[0]) 
print(s[17])
print(s[6])

print(s[-1])
print(s[-18])
print(s[-7])
print(s[-0])
print(s[17:])

# string slicing
s = 'Hello out there!'
print(s[:5])
print(s[6:9])
print(s[10:])
print(s[:-1])
print(s[0:10:2])
print(s[-6:-1])

# input exercise
print("What is your name ?")
name = input()
print("Hi", name, "!")

print("What is your name?")
name = input()
print(len(name))
print(name[-2:])