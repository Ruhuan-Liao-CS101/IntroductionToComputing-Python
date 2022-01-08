import json
import requests

strAPI = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2020-10-27&end_date=2020-10-27&api_key=gx1daXuj2m8vbtrVKtHALsIVu8U2yvBOWcbyjch8"

response = requests.get( strAPI )

json_data = json.loads(response.text)

# retrieve the previous link
print( json_data["links"]["prev"] )

# retrieve a name of the asteroids
print( json_data["near_earth_objects"]["2020-10-27"][0]["name"] )

for neo in json_data["near_earth_objects"]["2020-10-27"]:
    print( neo["name"] )

for i in range( len(json_data["near_earth_objects"]["2020-10-27"] )):
    print( json_data["near_earth_objects"]["2020-10-27"][i]["name"] )

i=0
while i < json_data["element_count"]:
    print( json_data["near_earth_objects"]["2020-10-27"][i]["name"] )
    i += 1

# retrieve the estimated_diameter_min and estimated_diameter_max (in feet) of all the observed neos
print( json_data["near_earth_objects"]["2020-10-27"][0]["estimated_diameter"]["feet"] )

for neo in json_data["near_earth_objects"]["2020-10-27"]:
    print( neo["estimated_diameter"]["feet"] )

# retrieve the miss_disyance (in miles) of all the observed neos
print( json_data["near_earth_objects"]["2020-10-27"][0]["close_approach_data"][0]["miss_distance"]['miles'] )

for neo in json_data["near_earth_objects"]["2020-10-27"]:
    print( neo["close_approach_data"][0]["miss_distance"]['miles'] )
