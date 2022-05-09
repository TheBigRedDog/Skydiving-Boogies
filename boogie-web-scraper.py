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
time.sleep(2)

boogies = driver.find_elements(by=By.CLASS_NAME, value='mx-template.mx-product-details-template')
# TODO: IMPLEMENT SEPARATE PARSING FUNCTIONS FOR BOOGIE CONTACT INFO IN CASE IT IS ABSENT IN FUTURE BOOGIE ENTRIES
def parse_boogie_contact_info(boogie_soup_object, boogie_info):
    boogie_contact_info = boogie_soup.find(class_='col-sm-4')
    counter = 0
    boogie_dropzone = boogie_contact_info.find(class_='fa fa-plane')\
        .next_sibling.next_sibling
    boogie_location = boogie_contact_info.find(class_='fa fa-plane')\
        .next_sibling.next_sibling.next_sibling.split()
    boogie_main_contact = boogie_contact_info.find(class_='fa fa-user')\
        .next_sibling.text.strip().split(', ')[0]
    boogie_phone_number = boogie_contact_info.find(class_='fa fa-phone')
    if boogie_phone_number != None:
        boogie_phone_number = boogie_phone_number\
            .next_sibling.next_sibling.text.strip()
    boogie_email = boogie_contact_info.find(class_='fa fa-envelope')\
        .next_sibling.next_sibling.text.strip()
    boogie_link = boogie_contact_info.find(class_='fa fa-external-link')\
        .next_sibling.next_sibling.text.strip()
    print(boogie_link)
    # for child in boogie_contact_info.children:
    #     if len(child.find_all)
    #     text = child.text.strip()
    #     print(text)

    return boogie_contact_info

for boogie in boogies:
    boogie_info = {}
    boogie_html = boogie.get_attribute('outerHTML')
    boogie_soup = BeautifulSoup(boogie_html, 'html5lib')
    
    boogie_info['name'] = boogie_soup.find(class_='col-sm-7').contents[1].text.strip()
    boogie_info['dates'] = boogie_soup.find(class_='col-sm-5')\
        .contents[1].contents[1].contents[2]\
        .text.strip().replace("\n", "").split(' - ')
    parse_boogie_contact_info(boogie_soup, boogie_info)
  
    #1 = location
    #3 = main contact
    #
    #4




'''
USPA website is a shitshow. 
Classes for boogie divs is as follows:
boogie_name = "col-sm-7"
boogie_dates = "col-sm-5"
boogie_contact_info = "col-sm-4"
boogie_description = "col-sm-8"
'''