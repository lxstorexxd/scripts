from selenium import webdriver
import chromedriver_binary
import time


while True:
    browser = webdriver.Chrome()
    browser.get('https://вологда.рф/vote_student/')
    time.sleep(2)
    element = browser.find_element_by_id('vote_radio_29_132').click()
    time.sleep(2)
    element2 = browser.find_element_by_class_name('btn.btn-dark.title-normal').click()
    time.sleep(1)
    browser.close()