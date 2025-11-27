from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.kabum.com.br/")

time.sleep(2)

barra = driver.find_element("name", "q")
barra.send_keys("Ps5")
barra.send_keys(Keys.RETURN)

time.sleep(25)
driver.quit