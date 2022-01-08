# a randomly generated number with 5 guesses from the user.
# (1) set limits on number to be guessed. (2) get random number. (Hint: ranndomNumber = random.randint(1,99))
# (3) User input. 4) validate if the guessed number matches the random one.

# Break down requirements into tasks (I.e. business logic)
# Task 1 => generate a random number with in a range
# Task 2 => get number user
# Task 3 => compare user number with random number, communicate result of the validation
# Task 4 => keep track of user's guesses
# Task 5 => go back to task 2



import random
number = random.randint(1,99)
count = 1

while (count <= 5):
    guess = int(input("Enter an interger from 1 to 99 please: "))
    count = count + 1
    if guess > number:
        print("your guess was higher than the number")
    elif guess < number:
        print("your guess was lower than the number")
    elif guess == number:
        print("winner winner chicken dinner")
        break

if guess != number:
    print("Sorry, try again")
    print("The number was", number)
        
