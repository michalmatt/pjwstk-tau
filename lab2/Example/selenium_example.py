from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# driver = webdriver.Chrome(executable_path='D:\SeleniumWebDrivers\Chrome\chromedriver.exe')
s = Service('D:\SeleniumWebDrivers\Chrome\chromedriver.exe')
browser = webdriver.Chrome(service=s)

logger.info('Przechodzę na stronę Zalando')
# driver.get('https://www.zalando.pl/')
browser.get('https://www.zalando.pl/')
# temp = driver.find_element_by_class_name('z-navicat-header_navToolItemLink')
temp = browser.find_element(By.CLASS_NAME, 'z-navicat-header_navToolItemLink')
temp.click()
logger.warning('Jakieś ostrzeżenie')
# temp = driver.find_element_by_id('login.email')
temp = browser.find_element(By.ID, 'login.email')
temp.click()
temp.send_keys('login')
logger.error('Jakiś Error')

# driver.close()
browser.close()
