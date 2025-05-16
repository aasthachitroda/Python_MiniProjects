from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

to = '9920951469'
content = 'Happy Birthday Aastha'

chrome_driver_path = '/home/ubuntu/Aastha/Code/Python/PythonProjects/chromedriver_linux64/chromedriver'

options = Options()

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://web.whatsapp.com/send?phone=' + to + '&text=' + content)

time.sleep(15)

send_button = driver.find_element_by_xpath("//span[@data-icon='send']")
send_button.click()

driver.quit()
