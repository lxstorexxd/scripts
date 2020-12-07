from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.set_headless()
assert opts.headless

while True:
    browser = Firefox(options=opts)
    browser.get('https://вологда.рф/vote_student/')
    time.sleep(2)
    element = browser.find_element_by_id('vote_radio_29_127').click()
    time.sleep(2)
    element2 = browser.find_element_by_class_name('btn.btn-dark.title-normal').click()
    time.sleep(1)
    browser.close()