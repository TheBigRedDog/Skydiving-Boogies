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

def parse_boogie_dropzone(boogie_soup_object, boogie_info):
    boogie_dropzone_sibling = boogie_soup_object.find(class_='col-sm-4').find(class_='fa fa-plane')
    if boogie_dropzone_sibling != None:
        boogie_dropzone = boogie_dropzone_sibling\
            .next_sibling.next_sibling.text
        boogie_info['dropzone'] = boogie_dropzone
    else:
        boogie_info['dropzone'] = None

def parse_boogie_location(boogie_soup_object, boogie_info):
    boogie_location_sibling = boogie_soup_object.find(class_='col-sm-4').find(class_='fa fa-plane')
    if boogie_location_sibling != None:
        boogie_location = boogie_location_sibling\
            .next_sibling.next_sibling.next_sibling.split()
        boogie_info['city'] = boogie_location[0]
        boogie_info['state'] = boogie_location[1]
    else:
        boogie_info['city'] = None
        boogie_info['state'] = None

def parse_boogie_main_contact(boogie_soup_object, boogie_info):
    boogie_main_contact_sibling = boogie_soup_object.find(class_='col-sm-4').find(class_='fa fa-user')
    if boogie_main_contact_sibling != None:
        boogie_main_contact = boogie_main_contact_sibling\
            .next_sibling.text.strip().split(', ')[0]
        boogie_info['main_contact'] = boogie_main_contact
    else:
        boogie_info['main_contact'] = None

def parse_boogie_phone_number(boogie_soup_object, boogie_info):
    boogie_phone_number_sibling = boogie_soup_object.find(class_='col-sm-4').find(class_='fa fa-phone')
    if boogie_phone_number_sibling != None:
        boogie_phone_number = boogie_phone_number_sibling\
            .next_sibling.next_sibling.text.strip()
        boogie_info['boogie_phone_number'] = boogie_phone_number
    else:
        boogie_info['boogie_phone_number'] = None
    
def parse_boogie_email(boogie_soup_object, boogie_info):
    boogie_email_sibling = boogie_soup_object.find(class_='col-sm-4').find(class_='fa fa-envelope')
    if boogie_email_sibling != None:
        boogie_email = boogie_email_sibling\
            .next_sibling.next_sibling.text.strip()
        boogie_info['email'] = boogie_email
    else:
        boogie_info['email'] = None

def parse_boogie_link(boogie_soup_object, boogie_info):
    boogie_link_sibling = boogie_soup_object.find(class_='col-sm-4').find(class_='fa fa-external-link')
    if boogie_link_sibling != None:
        boogie_link = boogie_link_sibling\
            .next_sibling.next_sibling.text.strip()
        boogie_info['link'] = boogie_link
    else:
        boogie_info['link'] = None

def parse_boogie_name(boogie_soup_object, boogie_info):
    boogie_name_parent = boogie_soup_object.find(class_='col-sm-7')
    if boogie_name_parent != None:
        boogie_name = boogie_name_parent\
            .contents[1].text.strip()
        boogie_info['name'] = boogie_name
    else:
        boogie_info['name'] = None

def parse_boogie_dates(boogie_soup_object, boogie_info):
    boogie_dates_parent = boogie_soup_object.find(class_='col-sm-5')
    if boogie_dates_parent != None:
        boogie_dates = boogie_dates_parent\
            .contents[1].contents[1].contents[2]\
            .text.strip().replace("\n", "").split(' - ')
        boogie_info['start_date'] = boogie_dates[0]
        boogie_info['end_date'] = boogie_dates[1]
    else:
        boogie_info['start_date'] = None
        boogie_info['end_date'] = None

for boogie in boogies:
    boogie_info = {}
    boogie_html = boogie.get_attribute('outerHTML')
    boogie_soup = BeautifulSoup(boogie_html, 'html5lib')
    
    parse_boogie_name(boogie_soup, boogie_info)
    parse_boogie_dates(boogie_soup, boogie_info)
    parse_boogie_dropzone(boogie_soup, boogie_info)
    parse_boogie_location(boogie_soup, boogie_info)
    parse_boogie_main_contact(boogie_soup, boogie_info)
    parse_boogie_phone_number(boogie_soup, boogie_info)
    parse_boogie_email(boogie_soup, boogie_info)
    parse_boogie_link(boogie_soup, boogie_info)
    print(boogie_info)

    
  




'''
USPA website is a shitshow. 
Classes for boogie divs is as follows:
boogie_name = "col-sm-7"
boogie_dates = "col-sm-5"
boogie_contact_info = "col-sm-4"
boogie_description = "col-sm-8"
'''