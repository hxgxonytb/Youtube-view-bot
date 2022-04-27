# Hello, this is a bot to make views on TouTube. Don't abuse it and subscribe to my Youtube channel: hxgx

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://www.youtube.com/watch?v=a1me6-cLSdY&t=92s") # replace this link with your link of your video

while True:
    sleep(20)
    driver.refresh()





