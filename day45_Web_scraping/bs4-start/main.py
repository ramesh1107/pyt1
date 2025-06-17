from bs4 import BeautifulSoup
#import lxml
import requests

'''with open ("day45_Web_scraping/bs4-start/website.html", 'r') as file:
    contents = file.read()  

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)'''

requests.get("https://news.ycombinator.com/")
response = requests.get("https://news.ycombinator.com/")    
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')  
print(soup.title.string)
print(soup.prettify())