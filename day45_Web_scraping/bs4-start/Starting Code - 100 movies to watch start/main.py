import requests
from bs4 import BeautifulSoup

URL1 = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL ="https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

requests.get(URL)
response = requests.get(URL)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.title.string)
#print(soup.prettify())
# soup = BeautifulSoup(response.text, 'html.parser')
l=[]
l1=[]
all_movies = soup.find_all('h2')
#for h2 in h2_elements:
#    print(h2.text)
#l1= l.reverse()
#print(l)

mt= [movie.getText() for movie in all_movies]
movies= (mt[::-1])
#l1= l.reverse()

with open("day45_Web_scraping/bs4-start/100_movies/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
        #print(movie)
#print(movies)