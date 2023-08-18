import os
import time
# import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

os.environ['PATH'] += r'C:/Users/colby/OneDrive/Coding/Selenium Drivers'
driver = webdriver.Chrome(options=options)

driver.get('https://www.playnow.com/mb/sports/sport/3/football/matches')

time.sleep(3)

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.PAGE_DOWN*5)
show_more = driver.find_elements(
    By.XPATH, '//button[text()="Show More Events"]')
for element in show_more:
    element.send_keys(Keys.RETURN)

text = body.text
print(text)
