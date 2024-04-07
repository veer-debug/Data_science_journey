from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
# time.sleep(1)
# driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()

# time.sleep(2)
a=0
old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(3)

    new_height = driver.execute_script('return document.body.scrollHeight')

    print(old_height)
    print(new_height)
    print(a)

    if new_height == old_height:
        break

    old_height = new_height
    a+=1

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)