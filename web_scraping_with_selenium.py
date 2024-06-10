import selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(service = service, options = options)

#driver.get("https://google.com")
url = "https://www.mastersportal.com/"
driver.get(url)

what_search_box = driver.find_element(By.ID, 'HomeWhat')
what_search_box.send_keys("computer")
what_search_box.send_keys(Keys.ENTER)

where_search_box = driver.find_element(By.ID, 'HomeWhere')
where_search_box.send_keys("Canada")
what_search_box.send_keys(Keys.ENTER)

time.sleep(60)

driver.quit()