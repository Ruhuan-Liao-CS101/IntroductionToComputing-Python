class Article:

    def __init__( self, source_name, author, title, description ):
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description

    def print_article_info( self ):
        print("Source: " + self.source_name +
        "\n Title: " + self.title +
        "\n Author: " + self.author + "\n")