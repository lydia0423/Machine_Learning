
#?Take the code from the How To Decode A Website exercise 
#?(if you didn’t do it or just want to play with some different code, use the code from the solution), 
#?and instead of printing the results to a screen, write the results to a txt file. 
#?In your code, just make up a name for the file you are saving to.

#?Extras:
#?Ask the user to specify the name of the output file that will be saved.

from io import BufferedWriter
from bs4 import BeautifulSoup
import requests

n = input("Please enter the file you would like to saved with the extension .txt: ")

x = 'http://www.nytimes.com'
article = requests.get(x)
soup = BeautifulSoup(article.text, "html.parser")
title = []
for line in soup.find_all('h2'):
    if str(line.string) != "None":
        title.append(line.string.strip())


f = open(n, 'w')
for i in title:
    f.write(i.rstrip() + "\n")
    

