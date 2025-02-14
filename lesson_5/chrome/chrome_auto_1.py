from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))   # noqa: E501
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
search_input = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
search_input.send_keys(Keys.RETURN, Keys.RETURN,
                       Keys.RETURN, Keys.RETURN, Keys.RETURN)
delet = driver.find_elements(By.CSS_SELECTOR, ".added-manually")

print(len(delet))

sleep(5)
