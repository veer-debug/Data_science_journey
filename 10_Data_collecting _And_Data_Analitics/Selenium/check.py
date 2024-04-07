from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time




driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('http://youtube.com')

time.sleep(2)

user=driver.find_element(by=By.XPATH,value='/html/body/ntp-app//div/div[2]/ntp-realbox//div/input')
user.send_keys('campusx')
time.sleep(1)
user.send_keys(Keys.ENTER)