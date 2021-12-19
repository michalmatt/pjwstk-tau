from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

# Logger initiation & setup
logger = logging.getLogger('TAU lab2')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# Firefox webdriver loading
s = Service('D:\SeleniumWebDrivers\Firefox\geckodriver.exe')
browser = webdriver.Firefox(service=s)

# Firefox: Empik scenario #1
logger.info('Firefox | Empik | Scenariusz #1')
logger.info('Przechodzę na stronę Empik')
browser.get('https://www.empik.com/')
logger.info('Wyszukuję frazę "organek"')
temp = browser.find_element(By.CLASS_NAME, 'css-1vl1nnj-input-input-1')
temp.click()
temp.send_keys('organek')
temp.send_keys(Keys.ENTER)
logger.info('Nie udało mi się zidentyfikować pierwszego produktu z listy wyszukiwania, aby kontynuować scenariusz')
logger.info('Zamykam przeglądarkę')
browser.close()
