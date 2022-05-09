from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
options = Options()
options.headless = True
options.add_argument("window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get('https://uspa.org/Events')

boogie_option = driver.find_element(by=By.XPATH, value='//*[@id="BO"]')
boogie_option.click()

find_events_button = driver.find_element(by=By.XPATH, value='/html/body/form/div[4]/section[2]/div/div/div[10]/div[1]/div/div/div/div/div/form/input')
find_events_button.click()
time.sleep(5)

boogies = driver.find_elements(by=By.CLASS_NAME, value='mx-template.mx-product-details-template')
print(boogies)
