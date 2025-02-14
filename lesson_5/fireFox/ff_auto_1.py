from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))   # noqa: E501

driver.get("http://the-internet.herokuapp.com/entry_ad")
search_input = driver.find_element(By.CSS_SELECTOR, '[class="modal-footer"]')
sleep(3)

search_input.click()
sleep(2)

driver.quit()
