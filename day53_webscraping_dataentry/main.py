import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
Form_URL= "https://forms.gle/eryyS64QaDgKtqL5A"
WEB_URL="https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(WEB_URL)
soup = BeautifulSoup(response.text, "html.parser")  
price= soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
price_list = []
for i in price:
    price_list.append(i.text)

address_tags= soup.find_all("address") 
address_list = []
if address_tags:
    
    for tag in address_tags:
       #print(tag)
        
        address_text=tag.text
        address_list.append(address_text)
        
link= soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
link_list = []
for i in link:
    link_list.append(i.get("href")) 
    
#print(price_list)
#print(address_list)
#print(link_list)
clean_price_list = [p.replace('/mo', '') for p in price_list]
cp= [p.replace('+', '') for p in clean_price_list]
cp1 = [p.replace('1 bd', '') for p in cp]
clean_address_list = [item.strip() for item in address_list]    
clean_link_list = [item.strip() for item in link_list]


# Set up the Edge WebDriver
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)  # Keep the browser open after script execution
edge_options.add_argument("--start-maximized")  # Start the browser maximized
driver = webdriver.Edge(options=edge_options)   

# Open the Google Form
driver.get(Form_URL)
# Fill in the form fields
'''for i in range(len(cp1)):
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61HD"]/div[2]/div/div[2]/div[1]/div/div[1]/input')
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61HD"]/div[2]/div/div[2]/div[2]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61HD"]/div[2]/div/div[2]/div[3]/div/div[1]/input')
    
    price_field.send_keys(cp1[i])
    address_field.send_keys(clean_address_list[i])
    link_field.send_keys(clean_link_list[i])
    
    # Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61HD"]/div[2]/div/div[3]/div/button')
    submit_button.click()
    
    # Wait for the form to be submitted and the page to reload
    driver.implicitly_wait(5)'''
    
for i in range(min(len(cp1), len(clean_address_list), len(clean_link_list))):
    price = driver.find_element(By.XPATH,
                        value='//*[@id="mG61HD"]/div[2]/div/div[2]/div[1]/div/div[1]/input')
    address= driver.find_element(By.XPATH, 
                        value='//*[@id="mG61HD"]/div[2]/div/div[2]/div[2]/div/div[1]/input')
    link= driver.find_element(By.XPATH, 
                        value='//*[@id="mG61HD"]/div[2]/div/div[2]/div[3]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, 
                                value='//*[@id="mG61HD"]/div[2]/div/div[3]/div/button')
    price.send_keys(cp1[i])
    address.send_keys(clean_address_list[i])
    link.send_keys(clean_link_list[i])
    submit_button.click()
    time.sleep(2)  # Wait for the form to reload
    driver.get(Form_URL)  # Reload the form for next submission