from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
import time 
DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
options = Options()
options.headless = True
options.add_argument('window-size=1920,1200')

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get('https://uspa.org/Events')

boogie_option = driver.find_element(by=By.XPATH, value='//*[@id="BO"]')
boogie_option.click()

find_events_button = driver.find_element(by=By.XPATH, value='/html/body/form/div[4]/section[2]/div/div/div[10]/div[1]/div/div/div/div/div/form/input')
find_events_button.click()
time.sleep(5)

boogies = driver.find_elements(by=By.CLASS_NAME, value='mx-template.mx-product-details-template')

for boogie in boogies:

    boogie_html = boogie.get_attribute('outerHTML')
    boogie_soup = BeautifulSoup(boogie_html, 'html5lib')

    boogie_name = boogie_soup.find(class_='col-sm-7').contents[1].text
    


'''
USPA website is a shitshow. 
Classes for boogie divs is as follows:
boogie_name = "col-sm-7"
boogie_dates = "col-sm-5"
boogie_contact_info = "col-sm-4"
boogie_description = "col-sm-8"
'''