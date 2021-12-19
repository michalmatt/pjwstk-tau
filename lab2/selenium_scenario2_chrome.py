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

# Chrome webdriver loading
s = Service('D:\SeleniumWebDrivers\Chrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)

# Chrome: Empik scenario #2
logger.info('Chrome | Empik | Scenariusz #2')
logger.info('Przechodzę na stronę Empik')
browser.get('https://www.empik.com/')
logger.info('Przechodzę w menu do "Pomoc"')
temp = browser.find_element(By.CLASS_NAME, 'empikNav__menu-mobile-2')
temp.click()
# temp = browser.find_element(By.CLASS_NAME, 'css-1i919hk-input')
# temp.click()
# temp.send_keys('organek')
# temp.send_keys(Keys.ENTER)
# logger.info('Nie udało mi się zidentyfikować pierwszego produktu z listy wyszukiwania, aby kontynuować scenariusz')
# logger.info('Zamykam przeglądarkę')
# browser.close()
