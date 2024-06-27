from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
source=[]
for i in range (1,267):
    driver.get('https://www.flipkart.com/search?q=smartphones&page={}'.format(i))
   
    html = driver.page_source
    source.append(html)

    time.sleep(121)
    print(i)

