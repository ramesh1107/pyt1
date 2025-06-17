import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings("ignore")

edge_options = webdriver.EdgeOptions()
'''edge_options.add_argument("--ignore-certificate-errors")    
edge_options.add_argument("--ignore-urlfetcher-cert-requests")
edge_options.add_argument("--disable-web-security")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--disable-software-rasterizer")
edge_options.add_argument("--headless")# Disable software rasterizer to avoid WebGL fallback''' 
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)

response= requests.get("https://www.python.org")
driver.get("https://www.python.org")
driver.maximize_window()    
#wait = WebDriverWait(driver, 10)
evt= driver.find_elements(By.CSS_SELECTOR, value= ".event-widget time" ) 
evname= driver.find_elements(By.CSS_SELECTOR, value= ".event-widget li a" )

for event in evt:
    print(event.text)
    
for name in evname:
    print(name.text)

events= {}
for i in range(len(evt)):
    events[i]= {
        "time": evt[i].text,
        "event": evname[i].text
    }
print(events)

driver.quit()  # Close the browser    