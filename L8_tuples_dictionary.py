#tuples
tuple1 = ("apple", "orange", "mango")
print(tuple1)

tuple_values = (1, 2, 3)
a, b, c = tuple_values   		#a=1, b=2, c=3

#dictionary
d = {}
print(d)
d = {'k1':12, 'k2':11, 'k3':43}         # assign values to dictionary
print(d)
d['k4'] = 23        # add new values/keys
print(d)

if 'k2' in d:
    print("Found it! And the associated value is ", d['k2'])
else:
    print("Not there!")

