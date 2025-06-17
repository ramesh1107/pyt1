from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--ignore-certificate-errors")
edge_options.add_argument("--ignore-urlfetcher-cert-requests")
edge_options.add_argument("--disable-web-security")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--disable-software-rasterizer")
edge_options.add_argument("--headless")# Disable software rasterizer to avoid WebGL fallback
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
driver.get("https://books.toscrape.com/")    
driver.maximize_window()
wait = WebDriverWait(driver, 10)
#price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
#currency = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-symbol")))


price= driver.find_element(By.CLASS_NAME , value="price_color")
#currency= driver.find_element(By.CLASS_NAME , value="a-price-symbol")
print("XXX----XXXX")
p=price.text
print(p)

#print(currency.text)
#final_price= price.text + currency.text
print(f"The price of the macbook air on amazon  is: {p}")

driver.quit()  # Close the browser
#driver.implicitly_wait(10)  # Wait for elements to load
#driver.close