from bs4 import BeautifulSoup
#import lxml
import requests
 

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#day = input("Which day do you want to travel in yyyy-mm-dd format")
#print(day)

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)