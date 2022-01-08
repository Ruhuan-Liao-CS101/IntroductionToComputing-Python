import requests
import json

from newsapi_article import Article

response = requests.get("http://newsapi.org/v2/top-headlines?country=us&apiKey=6c5d28dd303a432e8de15efc70ce6999")
raw_data = json.loads(response.text)

# dictionary to store all the articles objects
articles_d = {}

for article in raw_data["articles"]:

    """ print( article["source"]["name"] )
    print( article["author"] )
    print( article["title"] + "\n" ) """
    articles_d[str(article["source"]["name"])] = Article( str(article["source"]["name"]), str(article["author"]), str(article["title"]), str(article["description"]))
    
for article in articles_d.values():
    article.print_article_info()


# write a user defined function that 
# - takes in input a keyword
# - search the title for that keyword
# - if there is a match print all the information related to the articles

keyword = "covid"

def search_title( keyword ):
    for article in articles_d.values():
        if keyword in article.title or (keyword in article.description):
            print( "I found it!" )
        else:
            print( "Not there" )

search_title(keyword)

# refactor your program to search the title and the description