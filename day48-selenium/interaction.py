import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore")

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
#
driver = webdriver.Edge(options=edge_options)

#response= requests.get("https://en.wikipedia.org/wiki/Main_Page")
#navigaye to the oage
#driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()    
#wait = WebDriverWait(driver, 10)
#ae= driver.find_element(By.CSS_SELECTOR, value= "#articlecount a" ) 
#art= driver.find_element(By.CSS_SELECTOR, value= "articlecount Special:Statistics  articles in  " ) 
#print (ae.text)
#print (art.text)
#ae.click() #click on the link
fname= driver.find_element(By.NAME, value= "fName" )
fname.send_keys("John") #type in the search box
lname= driver.find_element(By.NAME, value= "lName" )
lname.send_keys("Doe") #type in the search box
email= driver.find_element(By.NAME, value= "email" )
email.send_keys("john.doe@gmail.com")
submit= driver.find_element(By.CSS_SELECTOR, value= "form button" )
submit.click() #click on the link
#type in the search box
#ap= driver.find_element(By.LINK_TEXT, value= "Content portals" )
#ap.click() #click on the link

#search= driver.find_element(By.NAME, value= "search" )
#
#s= driver.find_element(By.NAME, value= "search" )
#s.send_keys("Python") #type in the search box
#keyboard inputs
#email.send_keys(Keys.RETURN) #press enter

#driver.quit()  # Close the browser