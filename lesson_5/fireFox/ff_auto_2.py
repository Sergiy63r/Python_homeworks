from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))   # noqa: E501

driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
search_input.send_keys("1000")
sleep(3)

search_input.clear()
sleep(3)

search_input.send_keys("999")
sleep(2)

driver.quit()
