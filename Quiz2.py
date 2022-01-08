# Create a program that builds a list of integers, find the smallest number and calculate the average.

# Prompt the user to enter 6 integers smaller than 42.
# Read the inputs from the user and create a list. When reading the input validate that they are smaller than 42. 
# If they are bigger ask the user to enter another integer.

integersList=[]
i = 1
while i <= 5+1:
    i += 1
    numbers = int(input("Please enter a number that is smaller than 42: "))
    if numbers <= 42:
        integersList.append(numbers)
    else:
        numbers = int(input("Your input is greater than 42, please enter another number that is smaller than 42: "))
        integersList.append(numbers)
    if i=='6':
        break
print(integersList)

# Find the biggest number from the list and print it into the output.
print("The biggerst number from the list is: ", max(integersList))

# Find the average for all the numbers in the list and print the result
print("The average for all the numbers in the list is ", sum(integersList)/len(integersList))


