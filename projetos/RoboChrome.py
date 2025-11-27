import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

#inicia o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#abrir o site
driver.get("http://www.casasbahia.com.br")
try:
    WebDriverWait(driver, 20).until(EC.title_contains("Casas barriga"))
    #clica nas coordenadas especificas
    x = 665
    y = 386
    pyautogui.click(x, y)
    time.sleep(30)
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()