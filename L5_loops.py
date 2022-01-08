# countdown from 10 to 1
i = 10
print("The loop is about to start")
while( i>=1 ):
    print(i)
    i = i-1 
print("The loop is over")

#print 0-19 w/ for loop
for i in range(20):
    print("i is now:", i)


# exercise 1: count by 3 from 3 to 1000

# with the while loop
i = 3
print("The loop is about to start")
while( i<=1000 ):
    print(i)
    i = i+3 
print("The loop is over")

# with the for loop
for i in range(3, 1000, 3):
    print(i)


# exercise 2: sum all numbers from 1 to 1000

# with the while loop
i = 1
sum = 0
while(i<1000):
    sum = sum + i
    i = i + 1
print(sum)

# with the for loop
i = 1
sum = 0
for i in range(1,1000):
    sum = sum + i 
    i = i + 1
print(sum)
