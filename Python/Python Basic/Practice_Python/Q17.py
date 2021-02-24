
#?Use the BeautifulSoup and requests Python packages to print out a list of all the article titles 
#?on the New York Times homepage.

#*BeautifulSoup: 
#*Python library for pulling data out of HTML and XML format
#* easily navigate, search, scrape, and modify the parsed HTML/XML content like above 
#*(bytes type) by treating everything in it as a Python Object

from bs4 import BeautifulSoup
import requests

def getArticle(x):
    #*fetch the web page
    article = requests.get(x)
    #*turn page into a BeautifulSoup object
    soup = BeautifulSoup(article.text, "html.parser")

    #*h2 stand for headings2 --can view it by right-clicking on the web page and select inspects 
    #*to view the structure of it
    for line in soup.find_all('h2'):
        if str(line.string) != "None":
            print(line.string)

getArticle('http://www.nytimes.com')   
