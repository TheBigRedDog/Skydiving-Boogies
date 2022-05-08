from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
options = Options()
options.headless = True
options.add_argument("window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

driver.get('https://uspa.org/Events')

boogie_option = driver.find_element_by_xpath('//input[id="BO"][name="BO"][type="checkbox"]')
boogie_option.click()