#exercise w/ dictionary
countries = {}
countries = {'FR':"France", 'IN':"India", 'MX':"Mexico", 'Ca':"Canada", 'CN':"China"}
print(countries)
for key, values in countries.items():
    print(key, values)

#printing all values -- lost the keys
countries_values = countries.values()
for value in countries_values:
    print(value)

#reveiw/answer
countries_items = countries.items()
for item in countries_items:
    print(item) 
#another approach using just keys
countries_keys = countries.keys()
print("\n", countries_keys)
for key in countries_keys:
    print(key, " ", countries[key])

#converting lists into dictionaries 
countriesL = [["US", "United States"],
                ["GB", "United Kingdom"],
                ["IT", "Italy"]]
print("\n", countriesL)
countries = dict(countriesL)
print("\n", countries)
print("\nThe country code IT corresponds to ", countries.get("IT"), " ", countries["IT"])

# embedded/sub dictionaries 
contacts = { "david" : 
            {"number":"111-111-1111", "address":"Happy st", "city":"Los Angeles"},

            "jill" : 
            {"number":"222-222-2222", "address":"Tired ave", "city":"New York City"},

            "katie" : 
            {"number":"333-333-3333", "address":"Angry rd", "city":"Fairfield"}}
print(contacts)

print("\nInformation from my contacts for david: ", contacts.get("david"))
print("\nDavid's address: ")
print(contacts.get("david").get("address"))      # considering contacts as an object
print(contacts["david"]["address"])         # using keys to get the address 

print("\nJill's phone number is: ")
print(contacts.get("jill").get("number"))
print(contacts["jill"]["number"])