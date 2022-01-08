import json
import requests

strAPI = "http://newsapi.org/v2/top-headlines?country=us&apiKey=6c5d28dd303a432e8de15efc70ce6999"

response = requests.get( strAPI )

json_data = json.loads(response.text)

# retrieve a name of news sources
print( json_data["articles"][0]["source"]["name"] )

for news in json_data["articles"]:
    print( news["source"]["name"] )

# retrieve the "description" and the "url" for the sources "CNN"
print( json_data["articles"][4]["description"] )
print( json_data["articles"][4]["url"] )

# retrieve the "description" and the "url" for the "The Washington Post"
print( json_data["articles"][11]["description"] )
print( json_data["articles"][11]["url"] )

# retrieve the "description" and the "url" for the "BBC News"
print( json_data["articles"][14]["description"] )
print( json_data["articles"][14]["url"] )
